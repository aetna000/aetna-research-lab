import os
from siao import Screen, Intent, Action, Outcome, Memory, StepTrace
from tasks import SYNTHETIC_TASKS

OUTPUT_DIR = 'outputs'
os.makedirs(OUTPUT_DIR, exist_ok=True)

def simulate_agent_decision(elements, memory_state):
    # Naive demo agent: always submits if button present
    for el in elements:
        if 'submit' in el['id']:
            intent = Intent(type='submit_form', cited_elements=[el['id']], confidence=0.9)
            action = Action(type='click', element_id=el['id'], evidence='Button label == Submit')
            return intent, action
    # Else, pick first button
    for el in elements:
        if el['type'] == 'button':
            intent = Intent(type='click_button', cited_elements=[el['id']], confidence=0.6)
            action = Action(type='click', element_id=el['id'])
            return intent, action
    return Intent(type='noop', cited_elements=[], confidence=0), Action(type='noop', element_id='')

def simulate_outcome(action, screen):
    if action.type == 'click' and action.element_id == 'submit':
        return Outcome(ui_change='form_submitted', result_state={'submitted': True})
    return Outcome(ui_change='no_effect', result_state={})

def run_task(task):
    print(f"\n== Task: {task['id']} ==")
    memory = Memory(state={})
    episode_log = []
    for si, step in enumerate(task['steps']):
        screen = Screen(elements=step['elements'])
        intent, action = simulate_agent_decision(step['elements'], memory.state)
        outcome = simulate_outcome(action, screen)
        trace = StepTrace(screen, intent, action, outcome, memory)
        episode_log.append(trace)
        print(trace.to_json())
    # Save log
    with open(os.path.join(OUTPUT_DIR, f"{task['id']}_trace.json"), 'w') as f:
        f.write('[\n' + ',\n'.join(trace.to_json() for trace in episode_log) + '\n]')

if __name__ == '__main__':
    for task in SYNTHETIC_TASKS:
        run_task(task)