#!/usr/bin/env python3
import json
import sys
from collections import Counter

def load_trace(path):
    with open(path, 'r') as f:
        return json.load(f)

def summarize(trace):
    failures = Counter()
    for step in trace:
        for b in step.get('boundary_failures', []):
            failures[b] += 1
    print(f"Steps: {len(trace)}\n")
    for k, v in failures.items():
        print(f"Boundary failure '{k}': {v} occurrence(s)")
    print()
    incomplete = [s for s in trace if not s.get('final_success', False)]
    print(f"Steps not marked as successful: {len(incomplete)}")
    for s in incomplete:
        print(f" - Step {s['step_id']}: {s.get('workflow_step','')} | Failures: {s.get('boundary_failures',[])}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 score_audit_trace.py examples/sample_trace.json")
        sys.exit(1)
    trace = load_trace(sys.argv[1])
    summarize(trace)