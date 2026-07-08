from dataclasses import dataclass, asdict
from typing import Optional
from enum import Enum
import json

class RetrievalOutcome(str, Enum):
    HIT = "HIT"
    MISS = "MISS"
    CROSS_BOUNDARY = "CROSS-BOUNDARY"
    OMIT = "OMIT"
    ERROR = "ERROR"

@dataclass
class RetrievalEvent:
    step_id: str
    timestamp: str  # ISO8601
    query: str      # NL or structured
    intended_scope: str  # e.g. 'user', 'session', 'context', 'tool'
    provenance: str      # e.g. file/path/framehash
    permission: Optional[str] = None
    outcome: RetrievalOutcome = RetrievalOutcome.HIT
    latency_ms: Optional[int] = None
    user_id: Optional[str] = None
    notes: Optional[str] = None

    def to_json(self) -> str:
        return json.dumps(asdict(self))