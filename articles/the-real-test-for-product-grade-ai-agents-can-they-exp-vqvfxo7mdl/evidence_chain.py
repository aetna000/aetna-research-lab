import sys
import json
from schema import EvidenceChainStep

def load_scenario(path):
    with open(path) as f:
        return json.load(f)

def log_step(step):
    print(json.dumps(step.to_dict(), ensure_ascii=False))

def mock_agent_step(screen_state, ui_elements):
    """
    Minimal stub: Fakes perception and produces a plausible intent and action.
    In a real system, this would parse and cite evidence.
    """
    intent = f"Interact with '{ui_elements[0]['label']}'"
    evidence = {
        'type': 'ui_element',
        'ref': ui_elements[0]['id'],
        'label': ui_elements[0]['label'],
        'region': ui_elements[0]['bbox']
    }
    action = {
        'type': 'click',
        'target': ui_elements[0]['id'],
        'desc': f"Click '{ui_elements[0]['label']}'"
    }
    return intent, [evidence], action

def main(scenario_path):
    scenario = load_scenario(scenario_path)
    chain = []
    for step_num, step in enumerate(scenario['steps']):
        screen_state = step['screen_state']
        ui_elements = step['ui_elements']
        # Agent perceives and outputs intent/evidence/action
        intent, cited_evidence, action = mock_agent_step(screen_state, ui_elements)
        # Simulate observed outcome (in real: would compare actual UI diff)
        outcome = {'screen_state': step.get('post_action_state', screen_state), 'status': 'ok'}
        ecs = EvidenceChainStep(
            step_num=step_num,
            screen_state=screen_state,
            ui_elements=ui_elements,
            inferred_intent=intent,
            cited_evidence=cited_evidence,
            action=action,
            outcome=outcome
        )
        log_step(ecs)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("USAGE: python evidence_chain.py examples/simple_scenario.json > output_chain.jsonl", file=sys.stderr)
        sys.exit(1)
    main(sys.argv[1])