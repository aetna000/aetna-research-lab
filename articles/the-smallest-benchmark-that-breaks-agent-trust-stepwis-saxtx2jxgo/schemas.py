from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any

@dataclass
class Screen:
    id: str
    image: str  # path or description for synthetic demo
    ui_state: Dict[str, Any]
    ambiguity: Optional[str] = None  # note for edge cases

@dataclass
class Intent:
    description: str
    source: str  # human, agent, or simulated
    confidence: float  # [0,1]

@dataclass
class Action:
    label: str
    params: Dict[str, Any]
    uncertainty: Optional[float] = None
    rationale: Optional[str] = None

@dataclass
class Outcome:
    success: bool
    new_state: Dict[str, Any]
    delta: Optional[Dict[str, Any]] = None  # what changed
    notes: Optional[str] = None

@dataclass
class EvidenceLink:
    screen: Screen
    intent: Intent
    action: Action
    outcome: Outcome
    evidence: Optional[str] = None  # pointer to log, screenshot, etc.

@dataclass
class EvidenceChain:
    workflow_id: str
    steps: List[EvidenceLink] = field(default_factory=list)
    # Methods for completeness checks could be added here.