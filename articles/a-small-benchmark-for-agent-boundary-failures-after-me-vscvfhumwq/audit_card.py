import json
from typing import List, Dict, Any

class AuditCard:
    def __init__(self,
                 claim: str,
                 evidence: Dict[str, Any],
                 memory_state: Dict[str, Any],
                 permission: Dict[str, Any],
                 action: str,
                 expected_outcome: str,
                 post_state: Dict[str, Any]):
        self.claim = claim
        self.evidence = evidence
        self.memory_state = memory_state
        self.permission = permission
        self.action = action
        self.expected_outcome = expected_outcome
        self.post_state = post_state
        self.failures = self.score_boundaries()

    def score_boundaries(self) -> List[str]:
        failures = []
        # Minimal scoring for demo (real code: expand per domain + step)
        if self.evidence['type'] == 'ui_observation' and 'button' in self.evidence['content'].lower() and 'intent' in self.claim.lower():
            # Ambiguous if claim is intent but evidence is only button
            failures.append('ambiguous_intent')
        if 'amount' in self.memory_state and self.memory_state['amount'] is not None:
            max_allowed = 5000
            if self.memory_state['amount'] > max_allowed:
                failures.append('policy_violation')
        # Permission mismatch: required vs. actual
        if self.permission['required'] != self.permission['actual']:
            failures.append('permission_gap')
        # Over-broad memory/state (toy demo: session_timeout should be True after timeout)
        if self.memory_state.get('session_timeout', False) and 'action' in self.claim:
            failures.append('stale_state')
        # Unverifiable outcome
        if 'error' in self.post_state and self.expected_outcome.lower() in self.post_state['error'].lower():
            failures.append('unverifiable_outcome')
        return failures

    def to_dict(self):
        return {
            'claim': self.claim,
            'evidence': self.evidence,
            'memory_state': self.memory_state,
            'permission': self.permission,
            'action': self.action,
            'expected_outcome': self.expected_outcome,
            'post_state': self.post_state,
            'failures': self.failures
        }

if __name__ == '__main__':
    # Example: Three workflow steps
    cards = [
        AuditCard(
            claim="User intends to approve transfer",
            evidence={"type": "ui_observation", "content": "Approve Transfer button is highlighted"},
            memory_state={"last_action": "entered amount", "session_timeout": False},
            permission={"required": "can_initiate_transfer", "actual": "user"},
            action="initiate_transfer",
            expected_outcome="Transfer approved",
            post_state={"transfer_status": "pending"}
        ),
        AuditCard(
            claim="Amount is within policy",
            evidence={"type": "memory", "content": "max allowed = 5000"},
            memory_state={"amount": 7000},
            permission={"required": "manager", "actual": "user"},
            action="proceed_transfer",
            expected_outcome="Transfer processed",
            post_state={"error": "Permission denied"}
        ),
        AuditCard(
            claim="Session still active for update",
            evidence={"type": "state", "content": "session_timer = 0:00:10 left"},
            memory_state={"session_timeout": True},
            permission={"required": "editor", "actual": "editor"},
            action="edit_record",
            expected_outcome="Record updated",
            post_state={"error": "Session expired"}
        ),
    ]
    for idx, card in enumerate(cards, 1):
        print(f"--- Audit Card {idx} ---")
        d = card.to_dict()
        for k, v in d.items():
            print(f"{k.capitalize()}: {v}")
        print()