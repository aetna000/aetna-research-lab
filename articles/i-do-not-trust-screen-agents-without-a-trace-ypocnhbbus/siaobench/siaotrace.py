import json
import time

class SIAOStep:
    def __init__(self, screen_img, ui_elements, inferred_intent, intent_evidence, action, action_evidence, outcome_img, outcome_diff, error_label=None):
        self.timestamp = time.time()
        self.screen_img = screen_img         # Could be a path/ref or simulated string
        self.ui_elements = ui_elements       # Parsed elements (list/dict)
        self.inferred_intent = inferred_intent
        self.intent_evidence = intent_evidence
        self.action = action
        self.action_evidence = action_evidence
        self.outcome_img = outcome_img
        self.outcome_diff = outcome_diff     # Description or structured diff
        self.error_label = error_label       # If breakdown, why (see Article failure tags)

    def asdict(self):
        return self.__dict__

class SIAOTrace:
    def __init__(self):
        self.steps = []
    
    def add_step(self, step: SIAOStep):
        self.steps.append(step)

    def to_json(self, path):
        out = [s.asdict() for s in self.steps]
        with open(path, 'w') as f:
            json.dump(out, f, indent=2)

    def summary(self):
        summary = {
            'total_steps': len(self.steps),
            'failures': {},
        }
        for s in self.steps:
            if s.error_label:
                summary['failures'].setdefault(s.error_label, 0)
                summary['failures'][s.error_label] += 1
        return summary