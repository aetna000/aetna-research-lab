import json
from typing import Optional, Dict, Any, List

class AuditCard:
    def __init__(self,
                 step_name: str,
                 claim: str,
                 evidence: str,
                 evidence_type: str,  # e.g. observation, inference, memory, permission, outcome
                 action: str,
                 expected_outcome: str,
                 permission_boundary: str,
                 post_action_state: Optional[str] = None):
        self.step_name = step_name
        self.claim = claim
        self.evidence = evidence
        self.evidence_type = evidence_type
        self.action = action
        self.expected_outcome = expected_outcome
        self.permission_boundary = permission_boundary
        self.post_action_state = post_action_state
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'step_name': self.step_name,
            'claim': self.claim,
            'evidence': self.evidence,
            'evidence_type': self.evidence_type,
            'action': self.action,
            'expected_outcome': self.expected_outcome,
            'permission_boundary': self.permission_boundary,
            'post_action_state': self.post_action_state
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2)

class AuditLog:
    def __init__(self):
        self.entries: List[AuditCard] = []
    
    def log(self, card: AuditCard):
        self.entries.append(card)
    
    def to_jsonl(self) -> str:
        return '\n'.join([c.to_json() for c in self.entries])
    
    def score_boundaries(self) -> Dict[str, int]:
        # Boundary types
        issues = {
            'missing_evidence': 0,
            'stale_state': 0,
            'ambiguous_intent': 0,
            'permission_gap': 0,
            'unverifiable_outcome': 0,
            'overbroad_memory': 0,
        }
        for card in self.entries:
            if not card.evidence:
                issues['missing_evidence'] += 1
            if card.evidence_type in ['memory', 'observation'] and card.post_action_state and card.post_action_state == 'stale':
                issues['stale_state'] += 1
            if 'maybe' in card.claim.lower() or 'unclear' in card.claim.lower():
                issues['ambiguous_intent'] += 1
            if card.permission_boundary != 'allowed':
                issues['permission_gap'] += 1
            if card.evidence_type == 'outcome' and (not card.post_action_state or 'unknown' in (card.post_action_state or '')):
                issues['unverifiable_outcome'] += 1
            if card.evidence_type == 'memory' and (card.permission_boundary == 'overbroad' or 'global' in card.permission_boundary):
                issues['overbroad_memory'] += 1
        return issues