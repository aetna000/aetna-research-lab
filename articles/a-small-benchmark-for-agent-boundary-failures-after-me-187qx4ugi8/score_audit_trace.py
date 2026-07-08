import sys
import json
from audit_card import score_audit_trace

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} EXAMPLE_TRACE.json")
        sys.exit(1)
    with open(sys.argv[1]) as fin:
        trace = json.load(fin)
    results = score_audit_trace(trace)
    for result in results:
        print(f"Step {result['step']}: {result['claim']}")
        if result['failures']:
            print(f"  Boundary failures: {', '.join(result['failures'])}")
        else:
            print("  All evidence boundaries satisfied.")