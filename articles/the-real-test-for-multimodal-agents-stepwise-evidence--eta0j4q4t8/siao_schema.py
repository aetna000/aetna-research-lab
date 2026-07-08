# Minimal SIAO evidence-chain schema
from typing import List, Dict, Any
from dataclasses import dataclass, asdict

@dataclass
class SIAOStep:
    screen_id: str                # unique screen/frame id
    screen_snapshot: str          # image filename or URI (synthetic)
    parsed_ui: Dict[str, Any]     # extracted UI elements, text
    inferred_intent: str          # agent's user/system intent
    intent_evidence: List[str]    # what on-screen supports the intent
    action: str                   # proposed action
    action_evidence: List[str]    # on-screen evidence for action
    outcome_snapshot: str         # image filename/URI after action
    state_delta: Dict[str, Any]   # what changed
    error_type: str               # none/grounding/intent/planning/attribution/execution
    notes: str

def step_to_json(step: SIAOStep):
    return asdict(step)