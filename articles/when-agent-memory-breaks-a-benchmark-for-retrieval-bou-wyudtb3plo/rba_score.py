import sys
import json
from collections import Counter

def load_events(path):
    with open(path, 'r', encoding='utf-8') as f:
        return [json.loads(line) for line in f if line.strip()]

def main():
    if len(sys.argv) < 2:
        print("Usage: python rba_score.py --input examples/example_trace.jsonl")
        sys.exit(1)
    in_path = sys.argv[sys.argv.index('--input')+1]
    events = load_events(in_path)
    outcome_counter = Counter(e['outcome'] for e in events)
    latencies = [e['latency_ms'] for e in events if 'latency_ms' in e]
    total = len(events)
    print(f"Total retrievals: {total}")
    for k in ['HIT','OMISSION','CROSS-BOUNDARY','AMBIGUOUS','ERROR']:
        v = outcome_counter.get(k,0)
        print(f"{k:>15}: {v} ({v/total:.1%})")
    if latencies:
        median = sorted(latencies)[len(latencies)//2]
        avg = sum(latencies)/len(latencies)
        print(f"Latency ms (median): {median:,.0f} | (avg): {avg:,.1f}")
    else:
        print("No latency data.")

if __name__ == '__main__':
    main()