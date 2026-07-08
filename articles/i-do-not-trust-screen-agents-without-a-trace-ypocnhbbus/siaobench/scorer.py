import json

def score_trace(path):
    with open(path) as f:
        steps = json.load(f)
    failures = {}
    for s in steps:
        if s.get('error_label'):
            failures[s['error_label']] = failures.get(s['error_label'], 0) + 1
    print(f"Total agent steps: {len(steps)}")
    if not failures:
        print("No failures labeled.")
    else:
        for tag, n in failures.items():
            print(f"{n} failure(s) of type: {tag}")

if __name__ == '__main__':
    import sys
    score_trace(sys.argv[1] if len(sys.argv) > 1 else 'siaotrace.json')