# Scoring for SIAO evidence-chain logs
import json
import sys

def score_evidence_chain(log_path, verbose=True):
    steps = [json.loads(line) for line in open(log_path)]
    n_steps = len(steps)
    missing_fields = 0
    error_counts = {}
    for step in steps:
        for key in ['screen_id','screen_snapshot','parsed_ui','inferred_intent','intent_evidence','action','action_evidence','outcome_snapshot','state_delta','error_type']:
            if step.get(key) is None or step.get(key) == '':
                missing_fields += 1
                if verbose:
                    print(f"Step {step.get('screen_id')} missing {key}")
        etype = step.get('error_type','none')
        error_counts[etype] = error_counts.get(etype,0)+1
    print(f"Total steps: {n_steps}")
    print(f"Incomplete fields: {missing_fields}")
    print(f"Failure type counts: {error_counts}")

if __name__ == "__main__":
    log_path = sys.argv[1] if len(sys.argv)>1 else 'out/evidence_chain_example.jsonl'
    score_evidence_chain(log_path)