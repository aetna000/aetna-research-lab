from dataclasses import dataclass, field, asdict
from typing import List, Optional, Dict, Any
import json

@dataclass
class Evidence:
    description: str
    region: Optional[str] = None
    ui_element_id: Optional[str] = None
    text: Optional[str] = None
    extra: Dict[str, Any] = field(default_factory=dict)

@dataclass
class SIAOStep:
    step_id: int
    screen_raw: str         # Path to screenshot image or JSON UI state
    parsed_ui: Dict[str, Any]  # Parsed UI map/elements
    focus: Optional[str]
    ambiguities: Optional[List[str]]
    intent: str             # Natural language intent statement
    intent_evidence: List[Evidence]
    action: str
    action_rationale: str
    action_evidence: List[Evidence]
    outcome: str            # e.g., UI diff or result
    outcome_diff: Optional[Dict[str, Any]]

@dataclass
class EvidenceChainLog:
    workflow_id: str
    steps: List[SIAOStep]

    def to_json(self):
        return json.dumps(asdict(self), indent=2)