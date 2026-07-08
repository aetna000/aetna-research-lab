import json
from evidence_schema import EvidenceChainStep
from trace_logger import EvidenceChainLogger

# Example fixture: load static UI state
with open('fixtures/example_ui_state.json') as f:
    ui_states = json.load(f)

logger = EvidenceChainLogger()

# Simulate two workflow steps
steps_data = [
    {
        'pre': ui_states[0],
        'intent': 'Submit login',
        'evidence': ['Button: "Sign In"', 'Input: username'],
        'action': 'Click "Sign In"',
        'rationale': 'All required fields are filled; submit is enabled.',
        'post': ui_states[1],
        'diff': 'screen moved to dashboard',
        'breakdown': None
    },
    {
        'pre': ui_states[1],
        'intent': 'Open notifications',
        'evidence': ['Bell icon present, no badge'],
        'action': 'Click bell icon',
        'rationale': 'User typically checks notifications after login.',
        'post': ui_states[2],
        'diff': 'notification panel shown',
        'breakdown': None
    }
]

for d in steps_data:
    step = EvidenceChainStep(
        pre_action_screen=d['pre'],
        inferred_intent=d['intent'],
        intent_evidence=d['evidence'],
        action=d['action'],
        action_rationale=d['rationale'],
        post_action_screen=d['post'],
        outcome_diff=d['diff'],
        breakdown_label=d['breakdown']
    )
    logger.add_step(step)

logger.save_trace('fixtures/example_run_trace.json')
print('Trace saved to fixtures/example_run_trace.json')