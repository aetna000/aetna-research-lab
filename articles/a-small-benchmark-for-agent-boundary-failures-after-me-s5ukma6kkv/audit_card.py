from dataclasses import dataclass, field, asdict
from typing import Optional, List, Dict, Any
import enum

class BoundaryType(enum.Enum):
    OBSERVATION = "observation"
    INFERENCE = "inference"
    PREFERENCE = "preference"
    INSTRUCTION = "instruction"
    PERMISSION = "permission"
    ACTION = "action"
    OUTCOME = "outcome"

@dataclass
class AuditCard:
    step_id: str
    workflow_step: str
    claim: str
    boundary_type: BoundaryType
    source_evidence: Optional[str] = None  # e.g., screenshot hash, UI element, memory ref
    memory_state: Optional[str] = None
    permission: Optional[str] = None  # e.g., allowed actions
    action: Optional[str] = None
    expected_outcome: Optional[str] = None
    post_action_observation: Optional[str] = None
    boundary_failures: List[str] = field(default_factory=list)
    notes: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["boundary_type"] = self.boundary_type.value
        return d

@dataclass
class AuditScorer:
    audit_cards: List[AuditCard]

    def score_boundaries(self) -> Dict[str, int]:
        failures = {
            'missing_evidence': 0,
            'stale_state': 0,
            'ambiguous_intent': 0,
            'permission_gap': 0,
            'unverifiable_outcome': 0,
            'overbroad_memory': 0
        }
        for card in self.audit_cards:
            for fail in card.boundary_failures:
                if fail in failures:
                    failures[fail] += 1
        return failures

    def overall_success(self) -> bool:
        return all(len(card.boundary_failures) == 0 for card in self.audit_cards)