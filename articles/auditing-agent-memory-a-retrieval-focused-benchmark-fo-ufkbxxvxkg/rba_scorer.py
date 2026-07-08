import json
from rba_schema import RetrievalEvent, RetrievalOutcome
from typing import List

SCORES = {
    RetrievalOutcome.HIT: 1,
    RetrievalOutcome.MISS: 0,
    RetrievalOutcome.CROSS_BOUNDARY: -1,
    RetrievalOutcome.OMIT: 0,
    RetrievalOutcome.ERROR: -2
}

def score_trace(events: List[RetrievalEvent], latency_threshold_ms=1500):
    total = 0
    details = []
    for ev in events:
        base = SCORES.get(ev.outcome, 0)
        slow = 0
        if ev.latency_ms is not None and ev.latency_ms > latency_threshold_ms:
            slow = -1
        score = base + slow
        details.append({
            "step_id": ev.step_id,
            "outcome": ev.outcome,
            "latency_ms": ev.latency_ms,
            "score": score
        })
        total += score
    return {"total_score": total, "num_events": len(events), "details": details}

if __name__ == "__main__":
    import sys
    from rba_logger import load_trace
    if len(sys.argv) != 2:
        print("USAGE: python rba_scorer.py examples/example_rba_trace.jsonl")
        exit(1)
    events = load_trace(sys.argv[1])
    result = score_trace(events)
    print(json.dumps(result, indent=2))