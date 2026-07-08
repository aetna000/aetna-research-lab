import json
from typing import List, Dict, Any

class SIAOStep:
    def __init__(self, step_id: int, pre_screen: str, parsed_ui: List[Dict[str, Any]],
                 intent: str, evidence: List[str], action: str, rationale: str, post_screen: str, outcome: str):
        self.step_id = step_id
        self.pre_screen = pre_screen  # e.g., path to screenshot or unique screen hash/ID
        self.parsed_ui = parsed_ui    # list of parsed UI elements or ambiguities
        self.intent = intent
        self.evidence = evidence      # cited UI tokens/segments supporting intent/rationale
        self.action = action
        self.rationale = rationale
        self.post_screen = post_screen  # e.g., path to screenshot after action
        self.outcome = outcome        # description or diff from prior state

    def to_dict(self):
        return {
            "step_id": self.step_id,
            "pre_screen": self.pre_screen,
            "parsed_ui": self.parsed_ui,
            "intent": self.intent,
            "evidence": self.evidence,
            "action": self.action,
            "rationale": self.rationale,
            "post_screen": self.post_screen,
            "outcome": self.outcome
        }

class SIAOChain:
    def __init__(self):
        self.steps = []

    def add(self, siao_step: SIAOStep):
        self.steps.append(siao_step)

    def to_json(self, path: str):
        with open(path, 'w') as f:
            json.dump([step.to_dict() for step in self.steps], f, indent=2)

    def from_json(self, path: str):
        with open(path, 'r') as f:
            data = json.load(f)
            self.steps = [SIAOStep(**step) for step in data]