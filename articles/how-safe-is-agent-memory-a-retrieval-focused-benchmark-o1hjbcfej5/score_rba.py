import json
import sys
from collections import Counter

def score_event(event):
    # Assign points according to Article scoring rubric
    if event["outcome"] == "HIT":
        return 1
    elif event["outcome"] == "OMISSION":
        return 0
    elif event["outcome"] in {"CROSS-BOUNDARY", "ERROR"}:
        return -1
    elif event["outcome"] == "MISS":
        return 0
    else:
        return 0

def print_report(events):
    total = 0
    scores = []
    boundary_failures = 0
    latencies = []
    unexplained = 0
    fail_clusters = Counter()
    for ev in events:
        score = score_event(ev)
        scores.append(score)
        total += score
        latencies.append(ev["latency_ms"])
        if score == -1:
            boundary_failures += 1
            fail_clusters[ev["retrieval_scope"]] += 1
        if ev["outcome"] == "ERROR":
            unexplained += 1
    print("Per-retrieval scores:")
    for i, (ev, s) in enumerate(zip(events, scores)):
        print(f"{i+1}. Step {ev['step_id']} [{ev['outcome']}] -> {s}")
    print("\nSummary:")
    print(f"  Total boundary failures: {boundary_failures}")
    print(f"  Average latency (ms): {sum(latencies)/len(latencies):.2f}")
    print(f"  Unexplained recalls (ERROR): {unexplained}")
    print(f"  Failure clusters by retrieval_scope: {dict(fail_clusters)}")
    print(f"  Total RBA score: {total}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python score_rba.py <rba_event_log.json>")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        events = json.load(f)
    print_report(events)

if __name__ == "__main__":
    main()