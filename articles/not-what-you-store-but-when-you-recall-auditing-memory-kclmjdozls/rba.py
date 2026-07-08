"""
Retrieval Boundary Audit (RBA) protocol implementation.

Classes:
    RetrievalEvent: single retrieval log entry
    AuditLog: collection of events for a workflow session
    AuditScorer: computes fidelity, boundary, latency, omission scores
"""

from dataclasses import dataclass, field, asdict
from typing import List, Optional, Dict, Any
from enum import Enum
import json
import time

class Outcome(Enum):
    HIT = "hit"
    MISS = "miss"
    CROSS_BOUNDARY = "cross_boundary"
    OMITTED = "omitted"
    ERROR = "error"

@dataclass
class RetrievalEvent:
    step_id: str
    timestamp: float
    query: str
    intended_scope: Dict[str, Any]  # e.g., {"user_id": "u1", "session_id": "s1"}
    provenance: Dict[str, Any]      # source metadata, screen hash, etc.
    latency_ms: float
    outcome: Outcome
    notes: Optional[str] = None

class AuditLog:
    """Collects and exports retrieval events for a session."""
    def __init__(self, session_id: str, agent_id: str):
        self.session_id = session_id
        self.agent_id = agent_id
        self.events: List[RetrievalEvent] = []

    def add_event(self, event: RetrievalEvent):
        self.events.append(event)

    def to_dict(self) -> Dict:
        return {
            "session_id": self.session_id,
            "agent_id": self.agent_id,
            "events": [asdict(e) for e in self.events]
        }

    def export(self, path: str):
        with open(path, 'w') as f:
            json.dump(self.to_dict(), f, indent=2)

class AuditScorer:
    """Scores a completed audit log along RBA dimensions."""
    def __init__(self, log: AuditLog):
        self.log = log

    def fidelity(self) -> float:
        """Fraction of retrieval events that were hits."""
        hits = sum(1 for e in self.log.events if e.outcome == Outcome.HIT)
        total = len(self.log.events)
        return hits / total if total > 0 else 0.0

    def boundary(self) -> float:
        """Fraction that did not cross boundaries (i.e., not CROSS_BOUNDARY)."""
        safe = sum(1 for e in self.log.events if e.outcome != Outcome.CROSS_BOUNDARY)
        total = len(self.log.events)
        return safe / total if total > 0 else 0.0

    def latency(self) -> float:
        """Mean retrieval latency in ms."""
        latencies = [e.latency_ms for e in self.log.events]
        return sum(latencies) / len(latencies) if latencies else 0.0

    def omission_traceability(self) -> float:
        """Fraction of omissions that were explicitly justified (not just missing).
        Here we simplify: if outcome is OMITTED and notes explains why, it's traceable.
        """
        omissions = [e for e in self.log.events if e.outcome == Outcome.OMITTED]
        if not omissions:
            return 1.0
        traceable = sum(1 for e in omissions if e.notes and "justified" in e.notes.lower())
        return traceable / len(omissions)

    def report(self) -> Dict[str, float]:
        return {
            "fidelity": self.fidelity(),
            "boundary_enforcement": self.boundary(),
            "latency_ms_mean": self.latency(),
            "omission_traceability": self.omission_traceability()
        }