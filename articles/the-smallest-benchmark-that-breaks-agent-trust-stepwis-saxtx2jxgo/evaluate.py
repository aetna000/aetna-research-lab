from schemas import EvidenceChain, EvidenceLink, Screen, Intent, Action, Outcome
from synthetic_ui import get_synthetic_ui_sequence

def dummy_agent(screen):
    # Pretend agent: log evidence step-by-step (simulate random missing link)
    from random import random
    intent_present = random() > 0.2
    action_present = random() > 0.2
    outcome_present = random() > 0.2
    return EvidenceLink(
        screen=screen,
        intent=Intent(description='Infer login', source='agent', confidence=0.95) if intent_present else None,
        action=Action(label='click', params={'button': 'Continue'}, rationale='Next step') if action_present else None,
        outcome=Outcome(success=True, new_state={'logged_in': True}) if outcome_present else None,
        evidence='SimLog/step.log' if all([intent_present, action_present, outcome_present]) else None
    )

def evaluate_chain():
    screens = get_synthetic_ui_sequence()
    steps = []
    for screen in screens:
        link = dummy_agent(screen)
        steps.append(link)
    chain = EvidenceChain(workflow_id='demo_workflow', steps=steps)
    print('Evidence Chain Completeness:')
    for i, step in enumerate(chain.steps):
        score = {
            'screen': step.screen.id if step.screen else 'MISSING',
            'intent': 'OK' if step.intent else 'MISSING',
            'action': 'OK' if step.action else 'MISSING',
            'outcome': 'OK' if step.outcome else 'MISSING',
            'evidence': 'OK' if step.evidence else 'PARTIAL/AMBIGUOUS'
        }
        print(f'Step {i+1}:', score)
    return chain

if __name__ == '__main__':
    evaluate_chain()