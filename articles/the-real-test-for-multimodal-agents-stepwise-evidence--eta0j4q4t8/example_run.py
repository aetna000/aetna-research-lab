# Simulated two-step SIAO trace generation for a synthetic UI task
import json
from siao_schema import SIAOStep, step_to_json
import os

os.makedirs('out', exist_ok=True)
evidence_file = 'out/evidence_chain_example.jsonl'
with open(evidence_file, 'w') as f:
    # Step 1: login screen
    step1 = SIAOStep(
        screen_id='login_001',
        screen_snapshot='login_screen.png',
        parsed_ui={'fields': ['username', 'password'], 'buttons': ['Sign In']},
        inferred_intent='User wants to log in',
        intent_evidence=['username field is empty', 'password field is empty'],
        action='Click on username field',
        action_evidence=['cursor near username box'],
        outcome_snapshot='login_screen_filled.png',
        state_delta={'username_focused': True},
        error_type='none',
        notes='Agent correctly focuses on username field.'
    )
    f.write(json.dumps(step_to_json(step1)) + '\n')

    # Step 2: error step, planning breakdown
    step2 = SIAOStep(
        screen_id='login_002',
        screen_snapshot='login_screen_filled.png',
        parsed_ui={'fields': ['username', 'password'], 'buttons': ['Sign In']},
        inferred_intent='User wants to submit form',
        intent_evidence=['username has value', 'password is empty'],
        action='Click Sign In button',
        action_evidence=['Sign In button enabled'],
        outcome_snapshot='login_screen_error.png',
        state_delta={'error_msg': 'Password required'},
        error_type='planning',
        notes='Agent skipped password input; planning miss.'
    )
    f.write(json.dumps(step_to_json(step2)) + '\n')

print(f"Trace written to {evidence_file}")