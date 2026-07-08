import json
import sys

from collections import Counter

def load_log(log_path):
    with open(log_path) as f:
        for l in f:
            yield json.loads(l)

def score_rbst(log_path):
    outcomes = []
    latencies = []
    for entry in load_log(log_path):
        outcome = entry.get("outcome", "?")
        outcomes.append(outcome)
        lat = entry.get("latency_ms")
        if lat is not None:
            latencies.append(lat)
    counter = Counter(outcomes)
    total = sum(counter.values())
    print(f"Total Retrievals: {total}")
    for o in ["HIT", "MISS", "CROSS"]:
        print(f"{o}: {counter[o]} ({counter[o]/total*100:.1f}%)")
    if latencies:
        latencies.sort()
        n = len(latencies)
        med = latencies[n//2] if n % 2 == 1 else 0.5*(latencies[n//2-1] + latencies[n//2])
        mean = sum(latencies) / n
        print(f"Median latency: {med:.1f} ms\nMean latency: {mean:.1f} ms")
    else:
        print("No latency data logged.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python score_rbst.py <rbst_log.jsonl>")
        exit(1)
    log_path = sys.argv[1]
    score_rbst(log_path)