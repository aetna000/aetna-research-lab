import time
import hashlib
import json
from typing import List, Dict, Optional

class MemoryFragment:
    def __init__(self, content: str, user: str, session: str, screen_hash: str, timestamp: float):
        self.content = content
        self.user = user
        self.session = session
        self.screen_hash = screen_hash
        self.timestamp = timestamp

class RetrievalLog:
    def __init__(self, query: str, start_time: float, end_time: float, retrieved: Optional[MemoryFragment],
                 boundary_violation: bool, violation_type: Optional[str]):
        self.query = query
        self.latency_ms = int((end_time - start_time)*1000)
        self.retrieved_content = retrieved.content if retrieved else None
        self.retrieved_user = retrieved.user if retrieved else None
        self.retrieved_session = retrieved.session if retrieved else None
        self.screen_hash = retrieved.screen_hash if retrieved else None
        self.memory_timestamp = retrieved.timestamp if retrieved else None
        self.boundary_violation = boundary_violation
        self.violation_type = violation_type

    def to_dict(self):
        return self.__dict__

class MRLBAHarness:
    def __init__(self, memory_store: List[MemoryFragment]):
        self.memory_store = memory_store
        self.audit_log = []

    def retrieve(self, query: Dict, current_user: str, current_session: str) -> RetrievalLog:
        """
        Query should include:
            - content (search text)
            - type: 'in-scope', 'out-of-scope', 'distractor'
        """
        start = time.time()
        # Naive retrieval: exact match for content, else None.
        retrieved = next((m for m in self.memory_store if m.content == query['content']), None)
        end = time.time()
        boundary_violation = False
        violation_type = None
        if retrieved:
            if not (retrieved.user == current_user and retrieved.session == current_session):
                boundary_violation = True
                violation_type = 'user' if retrieved.user != current_user else 'session'
        elif query['type'] == 'in-scope':
            # Omission: in-scope not found
            violation_type = 'omission'
        elif query['type'] == 'out-of-scope' and retrieved:
            boundary_violation = True
            violation_type = 'out-of-scope leak'
        log = RetrievalLog(query['content'], start, end, retrieved, boundary_violation, violation_type)
        self.audit_log.append(log)
        return log

    def save_audit_log(self, path: str):
        with open(path, 'w') as f:
            for log in self.audit_log:
                f.write(json.dumps(log.to_dict()) + '\n')