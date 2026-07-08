import json
from typing import List, Dict, Any

class EvidenceChainStep:
    def __init__(self, step_id: int, pre_screen: str, ui_map: Dict[str, Any], intent: str, evidence_refs: List[str], action: str, rationale: str, post_screen: str, outcome_diff: str, attribution: str = None, failure: str = None):
        self.step_id = step_id
        self.pre_screen = pre_screen  # e.g., 'screen1.png' or base64 or descriptor
        self.ui_map = ui_map  # e.g., {"buttons": ["OK", "Cancel"], ...}
        self.intent = intent
        self.evidence_refs = evidence_refs  # e.g., ["button:OK"]
        self.action = action
        self.rationale = rationale  # why the action was chosen, referencing evidence_refs
        self.post_screen = post_screen
        self.outcome_diff = outcome_diff  # description or ID of screen/state change
        self.attribution = attribution  # e.g., agent ID; optionally user/session
        self.failure = failure  # None or, e.g., "intent_inference"

    def to_dict(self):
        return {
            "step_id": self.step_id,
            "pre_screen": self.pre_screen,
            "ui_map": self.ui_map,
            "intent": self.intent,
            "evidence_refs": self.evidence_refs,
            "action": self.action,
            "rationale": self.rationale,
            "post_screen": self.post_screen,
            "outcome_diff": self.outcome_diff,
            "attribution": self.attribution,
            "failure": self.failure
        }

class EvidenceChain:
    def __init__(self):
        self.steps: List[EvidenceChainStep] = []

    def add_step(self, **kwargs):
        step = EvidenceChainStep(len(self.steps), **kwargs)
        self.steps.append(step)

    def to_json(self, path=None):
        data = [step.to_dict() for step in self.steps]
        if path:
            with open(path, "w") as f:
                json.dump(data, f, indent=2)
        return json.dumps(data, indent=2)

    def replay(self):
        for step in self.steps:
            print(f"=== Step {step.step_id} ===")
            print(f"Pre-screen: {step.pre_screen}")
            print(f"UI map: {step.ui_map}")
            print(f"Intent: {step.intent}")
            print(f"Evidence refs: {step.evidence_refs}")
            print(f"Action: {step.action}")
            print(f"Rationale: {step.rationale}")
            print(f"Post-screen: {step.post_screen}")
            print(f"Outcome diff: {step.outcome_diff}")
            print(f"Attribution: {step.attribution}")
            print(f"Failure: {step.failure}\n")

# Example usage (see example_synthetic.py for a full run)