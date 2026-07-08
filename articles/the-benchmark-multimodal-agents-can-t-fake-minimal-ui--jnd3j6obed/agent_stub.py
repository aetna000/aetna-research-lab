import json
from typing import Dict, Any

def process_screen(screen: Dict[str, Any]) -> Dict[str, Any]:
    # Naive rule-based agent
    step = {
        'screen_id': screen['screen_id'],
        'screen_state': { 'elements': screen['ui_elements'] },
        'inferred_intent': '',
        'intent_evidence': '',
        'proposed_action': '',
        'action_evidence': '',
        'executed_action': '',
        'outcome': ''
    }
    if screen['screen_id'] == 'login_1':
        step['inferred_intent'] = 'submit_login_form'
        step['intent_evidence'] = 'presence of username/password fields'
        step['proposed_action'] = 'click login_btn'
        step['action_evidence'] = 'UI element: login_btn'
        step['executed_action'] = 'clicked login_btn'
        step['outcome'] = 'transition to login_fail_2'
    elif screen['screen_id'] == 'login_fail_2':
        step['inferred_intent'] = 'handle_login_error'
        step['intent_evidence'] = 'error_msg element = "Incorrect password."'
        step['proposed_action'] = 'click retry_btn'
        step['action_evidence'] = 'UI element: retry_btn'
        step['executed_action'] = 'clicked retry_btn'
        step['outcome'] = 'returns to login_1 or halts'
    else:
        step['inferred_intent'] = 'unknown'
        step['intent_evidence'] = 'N/A'
        step['proposed_action'] = 'N/A'
        step['action_evidence'] = ''
        step['executed_action'] = ''
        step['outcome'] = ''
    return step