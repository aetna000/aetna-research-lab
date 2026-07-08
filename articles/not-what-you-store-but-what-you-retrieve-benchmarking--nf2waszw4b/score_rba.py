import sys
import json
from rba_schema import RetrievalBoundaryEvent

def load_events(path):
    with open(path, 'r') as f:
        for line in f:
            if line.strip():
                e = RetrievalBoundaryEvent.from_jsonline(line)
                e.validate()
                yield e

def score(events):
    outcome_counts = {'HIT': 0, 'MISS': 0, 'CROSS': 0, 'AMBIG': 0}
    provenance_gaps = 0
    total = 0
    latencies = []
    cross_list = []
    for e in events:
        total += 1
        oc = e.outcome
        if oc in outcome_counts:
            outcome_counts[oc] += 1
        else:
            outcome_counts['AMBIG'] += 1
        if not e.provenance or e.provenance == "":
            provenance_gaps += 1
        latencies.append(e.latency_ms)
        if oc == 'CROSS':
            cross_list.append(e)
    print(f"Total retrievals: {total}")
    print("Breakdown:", outcome_counts)
    print(f"Provenance gaps: {provenance_gaps} ({provenance_gaps/max(total,1):.2%})")
    print(f"Avg latency: {sum(latencies)//max(len(latencies),1)}ms | Max: {max(latencies) if latencies else None}ms")
    print(f"Boundary breaches (CROSS): {len(cross_list)}")
    if cross_list:
        print("\nSample CROSS events:")
        for e in cross_list[:3]:
            print(vars(e))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python score_rba.py logs/example_retrievals.jsonl")
        sys.exit(1)
    events = list(load_events(sys.argv[1]))
    score(events)