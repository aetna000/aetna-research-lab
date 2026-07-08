import time
from dataclasses import dataclass, asdict
from typing import Optional, List, Dict

@dataclass
class RetrievalEvent:
    query: str
    intended_boundary: str  # e.g., 'user', 'session', 'ui', 'workflow-step'
    provenance: str   # e.g., doc_id, screen_hash
    timestamp: float
    workflow_step: str
    outcome: str  # 'HIT', 'MISS', 'CROSS-BOUNDARY', 'OMITTED'
    latency_ms: Optional[float] = None
    notes: Optional[str] = None

def log_event_eventdict(event: RetrievalEvent) -> Dict:
    return asdict(event)

class RetrievalLogger:
    def __init__(self):
        self.events: List[RetrievalEvent] = []
    def log(self, event: RetrievalEvent):
        self.events.append(event)
    def as_dict(self):
        return [log_event_eventdict(ev) for ev in self.events]
    def clear(self):
        self.events = []