from siaobench.siaotrace import SIAOStep, SIAOTrace

# Simulated agent workflow (note: actual AI not invoked)
UI_STATES = [
    {'screen_img': 'screen_1.png', 'ui_elements': [{'type': 'button', 'label': 'Submit'}], 'user_visible': 'empty form'},
    {'screen_img': 'screen_2.png', 'ui_elements': [{'type': 'input', 'label': 'Name'}], 'user_visible': 'filled form'},
    {'screen_img': 'screen_3.png', 'ui_elements': [], 'user_visible': 'confirmation'}
]

def toy_agent(ui_state):
    # Insert minimal, obvious logic just for artifact-ing
    if ui_state['user_visible'] == 'empty form':
        return {
            'intent': 'Fill in form',
            'intent_ev': "Screen shows empty form", 
            'action': 'type_name',
            'action_ev': "UI element 'Name' missing input"
        }
    if ui_state['user_visible'] == 'filled form':
        return {
            'intent': 'Submit form',
            'intent_ev': "Screen shows form filled", 
            'action': 'click_submit',
            'action_ev': "UI shows 'Submit' button"
        }
    return {
        'intent': 'Confirm result',
        'intent_ev': "Screen changed, confirmation detected", 
        'action': 'none',
        'action_ev': "No further UI elements"
    }

def run_benchmark():
    trace = SIAOTrace()
    prev_ui = None
    for idx, ui in enumerate(UI_STATES):
        agent_decision = toy_agent(ui)
        # Simulate error label for demonstration on 2nd step
        error = None
        if idx == 1:
            error = 'intent inference failure'  # synthetic, for artifact only
        step = SIAOStep(
            screen_img=ui['screen_img'],
            ui_elements=ui['ui_elements'],
            inferred_intent=agent_decision['intent'],
            intent_evidence=agent_decision['intent_ev'],
            action=agent_decision['action'],
            action_evidence=agent_decision['action_ev'],
            outcome_img=f"post_{ui['screen_img']}",
            outcome_diff=f"UI changed for step {idx}",
            error_label=error
        )
        trace.add_step(step)
        prev_ui = ui
    trace.to_json('siaotrace.json')
    print('Trace written to siaotrace.json')
    print(trace.summary())

if __name__ == '__main__':
    run_benchmark()