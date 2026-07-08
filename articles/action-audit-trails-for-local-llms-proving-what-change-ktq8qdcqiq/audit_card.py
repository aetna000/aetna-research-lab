"""
Local LLM Action Audit Card protocol.

For every agent step on a local inference engine, record:
1. Input evidence (screen/UI/state snapshot)
2. Memory/context fed to the model
3. Workflow permission state
4. Proposed action with risk classification
5. Delta in workflow/state after action
6. Verification that the intended change occurred
"""

from dataclasses import dataclass, field, asdict
from typing import Any, Dict, Optional
import json


@dataclass
class AuditCard:
    """Single step audit record."""
    step_id: int
    input_evidence: str  # path to screenshot or description
    memory_context: str   # what was fed to the model
    permission: str       # e.g., "user", "workflow", "tool"
    proposed_action: str
    risk: str             # "low", "medium", "high"
    before_state: Optional[Dict[str, Any]] = None
    after_state: Optional[Dict[str, Any]] = None
    delta: Optional[Dict[str, Any]] = None
    outcome_verified: bool = False
    verification_notes: str = ""

    def record_delta(self, before: Dict[str, Any], after: Dict[str, Any]) -> None:
        """Store pre- and post-action state and compute delta."""
        self.before_state = before
        self.after_state = after
        self.delta = self._compute_delta(before, after)

    def verify_outcome(self, success: bool, notes: str = "") -> None:
        """Record whether the intended change occurred."""
        self.outcome_verified = success
        self.verification_notes = notes

    def _compute_delta(self, before: Dict, after: Dict) -> Dict[str, Any]:
        """Simple delta: keys added, removed, or changed."""
        delta = {}
        all_keys = set(before.keys()) | set(after.keys())
        for k in all_keys:
            if k not in after:
                delta[k] = {"removed": before[k]}
            elif k not in before:
                delta[k] = {"added": after[k]}
            elif before[k] != after[k]:
                delta[k] = {"from": before[k], "to": after[k]}
            # else unchanged, omit
        return delta

    def to_dict(self) -> Dict[str, Any]:
        """Return a serializable dict for logging."""
        return asdict(self)

    def to_json(self) -> str:
        """Return JSON string."""
        return json.dumps(self.to_dict(), indent=2)

    def is_auditable(self) -> bool:
        """Check if all required fields are present."""
        required_fields = [
            self.input_evidence,
            self.memory_context,
            self.permission,
            self.proposed_action,
            self.risk,
        ]
        return all(required_fields) and self.delta is not None and self.outcome_verified