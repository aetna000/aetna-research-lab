import json
import sys
from mrlba_schema import RetrievalLog, score_retrieval

def main(trace_path):
    with open(trace_path, 'r') as f:
        trace = json.load(f)
    print("Step\tBoundaryError\tLatencyError\tMissingProvenance\tLatencyMs")
    for entry in trace['retrievals']:
        log = RetrievalLog(**entry)
        log.compute_latency()
        s = score_retrieval(log)
        print(f"{log.step_id}\t{s['boundary_error']}\t{s['latency_error']}\t{s['missing_provenance']}\t{log.latency_ms}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python mrlba_runner.py --trace <file.json>')
        sys.exit(1)
    trace_path = sys.argv[2] if sys.argv[1] == '--trace' else sys.argv[1]
    main(trace_path)