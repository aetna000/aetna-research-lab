from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum
from datetime import datetime

class BoundaryScope(str, Enum):
    IN_SCOPE = 'in_scope'
    OUT_OF_SCOPE = 'out_of_scope'
    AMBIGUOUS = 'ambiguous'

class AuditScore(str, Enum):
    SAFE = 'safe'
    WEAK = 'weak'
    FAIL = 'fail'

@dataclass
class Provenance:
    user_id: str
    session_id: str
    tool_id: str
    source: str  # e.g., 'chat_log', 'file_upload', etc.
    timestamp: str  # ISO8601

@dataclass
class RetrievalEvent:
    query: str
    query_scope: BoundaryScope
    query_start: str  # ISO8601
    retrieval_finish: str  # ISO8601
    retrieved_memory: Optional[str]
    provenance: Optional[Provenance]
    boundary_match: bool  # Did retrieved memory match in-scope expectations?
    leak_detected: bool
    ambiguous_provenance: bool
    latency_ms: Optional[int] = None

@dataclass
class AuditStep:
    step_num: int
    screen_context: str
    user_id: str
    session_id: str
    tool_id: str
    retrieval_events: List[RetrievalEvent]
    audit_score: AuditScore
    anomaly_flags: List[str] = field(default_factory=list)

@dataclass
class AuditRun:
    workflow_id: str
    audit_steps: List[AuditStep]
    trustworthy: bool  # Only if all steps are 'safe'
    run_time: str  # ISO8601 summary timestamp