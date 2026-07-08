import json
from typing import List, Dict, Any

# Core schema for one evidence-chain step
EVIDENCE_STEP_SCHEMA = {
    'required': ['screen_id', 'screen_state', 'inferred_intent', 'intent_evidence', 'proposed_action', 'action_evidence', 'executed_action', 'outcome'],
    'optional': ['ambiguity_flags', 'confidence_scores', 'reasoning']
}

def validate_step(step: Dict[str, Any]) -> bool:
    for key in EVIDENCE_STEP_SCHEMA['required']:
        if key not in step:
            print(f"Missing required field: {key}")
            return False
    return True

def validate_trace(trace_path: str) -> bool:
    with open(trace_path) as f:
        trace = json.load(f)
    for i, step in enumerate(trace['steps']):
        if not validate_step(step):
            print(f"Trace step {i} invalid.")
            return False
    print("Trace schema validated.")
    return True