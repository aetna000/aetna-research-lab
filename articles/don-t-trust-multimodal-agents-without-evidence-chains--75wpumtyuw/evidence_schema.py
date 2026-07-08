from typing import Any, Dict, List, Optional

class EvidenceChainStep:
    def __init__(self,
                 pre_action_screen: Dict[str, Any],
                 inferred_intent: str,
                 intent_evidence: List[str],
                 action: str,
                 action_rationale: str,
                 post_action_screen: Optional[Dict[str, Any]],
                 outcome_diff: Optional[str],
                 breakdown_label: Optional[str]):
        self.pre_action_screen = pre_action_screen
        self.inferred_intent = inferred_intent
        self.intent_evidence = intent_evidence
        self.action = action
        self.action_rationale = action_rationale
        self.post_action_screen = post_action_screen
        self.outcome_diff = outcome_diff
        self.breakdown_label = breakdown_label

    def as_dict(self):
        return {
            'pre_action_screen': self.pre_action_screen,
            'inferred_intent': self.inferred_intent,
            'intent_evidence': self.intent_evidence,
            'action': self.action,
            'action_rationale': self.action_rationale,
            'post_action_screen': self.post_action_screen,
            'outcome_diff': self.outcome_diff,
            'breakdown_label': self.breakdown_label
        }