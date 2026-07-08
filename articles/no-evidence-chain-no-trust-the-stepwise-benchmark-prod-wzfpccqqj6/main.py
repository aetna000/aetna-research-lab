import json
from schema import SIAOStep, Evidence, EvidenceChainLog

with open('sample_workflow.json', 'r') as f:
    workflow = json.load(f)

steps = []
for idx, (screen, truth) in enumerate(zip(workflow['screens'], workflow['ground_truth'])):
    step = SIAOStep(
        step_id=screen['step_id'],
        screen_raw=screen['screen_raw'],
        parsed_ui=screen['ui'],
        focus=None,  # For demo: focus assignment can be automated in live stack
        ambiguities=None,
        intent=truth['intent'],
        intent_evidence=[Evidence(**ev) for ev in truth['intent_evidence']],
        action=truth['action'],
        action_rationale=truth['action'],  # In real use, provide rationale as explanation
        action_evidence=[Evidence(**ev) for ev in truth['action_evidence']],
        outcome=truth['outcome'],
        outcome_diff=None
    )
    steps.append(step)

eclog = EvidenceChainLog(workflow_id=workflow['workflow_id'], steps=steps)
with open('output_log.json', 'w') as f:
    f.write(eclog.to_json())
print('Evidence-chain log written to output_log.json')