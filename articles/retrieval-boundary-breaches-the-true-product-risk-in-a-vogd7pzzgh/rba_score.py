import json
import argparse

SCORES = {
    'HIT': 1,
    'MISS': 0,  # Omitted, but boundary held
    'OMIT': 0,
    'CROSS-BOUNDARY': -1,
    'ERROR': -1
}

def score_log(logfile):
    total = 0
    count = 0
    boundary_errors = 0
    provenance_errors = 0
    result_counts = {k:0 for k in SCORES}
    latencies = []
    with open(logfile) as f:
        for line in f:
            event = json.loads(line)
            res = event['retrieval_result']
            score = SCORES.get(res, 0)
            total += score
            count += 1
            if res == 'CROSS-BOUNDARY' or res == 'ERROR':
                boundary_errors += 1
            result_counts[res] = result_counts.get(res, 0) + 1
            if 'latency_ms' in event: latencies.append(event['latency_ms'])
    print(f'RBA SCORE: {total}/{count}')
    print(f'Events by Result: {result_counts}')
    print(f'Boundary/Provenance errors: {boundary_errors}')
    if latencies:
        print(f'Average Latency (ms): {sum(latencies)//len(latencies)}')
    else:
        print('No latency data')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Score RBA Log')
    parser.add_argument('--input', type=str, required=True)
    args = parser.parse_args()
    score_log(args.input)