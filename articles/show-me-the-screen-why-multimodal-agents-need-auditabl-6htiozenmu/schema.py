from typing import Dict, Any

class EvidenceStep:
    def __init__(self, screen_image_path: str, ui_structure: Dict[str, Any], inferred_intent: str,
                 action: str, rationale: str, outcome_label: str, next_screen_image_path: str = None):
        self.screen_image_path = screen_image_path  # Path to screenshot (PNG/JPG)
        self.ui_structure = ui_structure  # Dict or JSON blob describing the UI parse
        self.inferred_intent = inferred_intent  # Agent's declared user intent at this step
        self.action = action  # The action taken (e.g., click, fill)
        self.rationale = rationale  # Rationale for action as provided by agent
        self.outcome_label = outcome_label  # e.g. 'success', 'failure', or state description
        self.next_screen_image_path = next_screen_image_path  # Optionally link diffed screenshot

class EvidenceChainEpisode:
    def __init__(self, steps):
        self.steps = steps  # List of EvidenceStep, ordered