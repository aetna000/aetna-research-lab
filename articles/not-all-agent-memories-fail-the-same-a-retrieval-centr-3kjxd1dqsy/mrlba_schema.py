import enum
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional
import datetime

class RetrievalBoundary(enum.Enum):
    IN_BOUNDS = "in-bounds"
    CROSS_SESSION = "cross-session"
    CROSS_USER = "cross-user"
    STALE = "stale"
    MISSING = "missing"

@dataclass
class RetrievalLog:
    step_id: str
    timestamp_query: str  # ISO8601
    timestamp_response: str  # ISO8601
    user_id: str
    session_id: str
    retrieval_query: str
    retrieved_fragment: str
    provenance: Dict[str, str]  # e.g., screen_hash, data_id, source_time
    boundary_label: str  # see RetrievalBoundary
    permission_flag: Optional[str] = None  # e.g., allowed/denied/ambiguous
    notes: Optional[str] = None
    latency_ms: Optional[int] = None

    def compute_latency(self):
        try:
            t_start = datetime.datetime.fromisoformat(self.timestamp_query)
            t_end = datetime.datetime.fromisoformat(self.timestamp_response)
            self.latency_ms = int((t_end - t_start).total_seconds() * 1000)
        except Exception:
            self.latency_ms = None

# Utility: Score a retrieval log for audit errors
def score_retrieval(log: RetrievalLog):
    score = {
        "boundary_error": log.boundary_label != RetrievalBoundary.IN_BOUNDS.value,
        "latency_error": log.latency_ms is not None and log.latency_ms > 1000,
        "missing_provenance": not (log.provenance and "screen_hash" in log.provenance)
    }
    return score