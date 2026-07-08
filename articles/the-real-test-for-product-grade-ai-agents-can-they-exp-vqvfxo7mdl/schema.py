class EvidenceChainStep:
    def __init__(self, step_num, screen_state, ui_elements, inferred_intent, cited_evidence, action, outcome):
        self.step_num = step_num
        self.screen_state = screen_state
        self.ui_elements = ui_elements
        self.inferred_intent = inferred_intent
        self.cited_evidence = cited_evidence
        self.action = action
        self.outcome = outcome

    def to_dict(self):
        return {
            'step_num': self.step_num,
            'screen_state': self.screen_state,
            'ui_elements': self.ui_elements,
            'inferred_intent': self.inferred_intent,
            'cited_evidence': self.cited_evidence,
            'action': self.action,
            'outcome': self.outcome
        }