import json

def audit_trace(trace_path):
    with open(trace_path, 'r') as f:
        steps = json.load(f)
    findings = []
    for i, step in enumerate(steps):
        msg = f'Step {i}: '
        # Example checks
        if step['intent']['cited_elements']:
            msg += 'Intent cites UI element(s). '
        else:
            msg += 'MISSING: Intent does not cite elements. '
        if step['action']['element_id'] in [el['id'] for el in step['screen']['elements']]:
            msg += 'Action element found in screen.'
        else:
            msg += 'MISMATCH: Action not in screen.'
        findings.append(msg)
    return findings

# Example usage:
# print('\n'.join(audit_trace('outputs/form_submit_distraction_trace.json')))