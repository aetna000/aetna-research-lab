import json
import sys
from schema import validate_trace

def check_attribution(trace_path):
    with open(trace_path) as f:
        trace = json.load(f)
    for i, step in enumerate(trace['steps']):
        missing = []
        for field in ['intent_evidence', 'action_evidence']:
            if not step.get(field):
                missing.append(field)
        if missing:
            print(f"Warning: Step {i} ({step.get('screen_id', '?')}) missing {', '.join(missing)}.")
    print("Evaluation complete.")

if __name__ == '__main__':
    # Usage: python evaluate_trace.py output/example_trace.json
    if len(sys.argv) != 2:
        print("Usage: python evaluate_trace.py [trace_path]")
        exit(1)
    validate_trace(sys.argv[1])
    check_attribution(sys.argv[1])