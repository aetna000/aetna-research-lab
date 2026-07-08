import json
from typing import List
from evidence_schema import EvidenceChainStep

class EvidenceChainLogger:
    def __init__(self):
        self.steps: List[EvidenceChainStep] = []

    def add_step(self, step: EvidenceChainStep):
        self.steps.append(step)

    def save_trace(self, filepath: str):
        """Save the entire trace in replayable JSON format."""
        trace_dict = [step.as_dict() for step in self.steps]
        with open(filepath, "w") as f:
            json.dump(trace_dict, f, indent=2)

    def reset(self):
        self.steps = []