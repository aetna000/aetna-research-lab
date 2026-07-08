import json

# Load ARRB test trace from json file (example format: see example_trace.json)
def load_trace(path):
    with open(path, 'r') as f:
        return json.load(f)

def score_trace(trace):
    total_steps = len(trace)
    false_recall_count = 0
    recall_miss_count = 0
    for ep in trace:
        # Ground truth
        should_recall = set(ep['ground_truth']['should_recall'])
        should_not_recall = set(ep['ground_truth']['should_not_recall'])
        agent_retrieved = set(ep['agent_retrieved'])
        # False recalls: agent retrieved forbidden
        false_recalls = agent_retrieved & should_not_recall
        # Recall misses: agent missed a required memory
        recall_misses = should_recall - agent_retrieved
        false_recall_count += len(false_recalls)
        recall_miss_count += len(recall_misses)
    print(f"Total steps: {total_steps}")
    print(f"False recall rate: {false_recall_count/total_steps:.2f} per step")
    print(f"Recall miss rate: {recall_miss_count/total_steps:.2f} per step")

if __name__ == "__main__":
    # Example: score a sample trace
    trace = load_trace("example_trace.json")
    score_trace(trace)