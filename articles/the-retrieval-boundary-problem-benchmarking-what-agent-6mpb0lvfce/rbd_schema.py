from dataclasses import dataclass, field
from typing import List, Dict, Optional

@dataclass
class RetrievalEvent:
    item_id: str                  # Unique identifier for memory/evidence
    source: str                   # e.g., 'short-term', 'external kb', 'user-session'
    used: bool                    # True if retrieved and used in agent reasoning
    omitted: bool                 # True if intentionally NOT retrieved
    omission_reason: Optional[str] = None   # Policy, session, privacy, deletion, etc.

@dataclass
class BoundaryEvent:
    event_type: str              # 'user_switch', 'workflow_transition', 'permission_change'
    details: Dict[str, str]
    timestamp: str

@dataclass
class StepLog:
    step_id: int
    timestamp: str
    context: Dict[str, str]                   # e.g. session, user, permission state
    retrieval_events: List[RetrievalEvent]
    boundary_event: Optional[BoundaryEvent] = None
    agent_action: str
    notes: Optional[str] = None

@dataclass
class WorkflowTrace:
    trace_id: str
    steps: List[StepLog]