import json
import sys
from agent_stub import process_screen

def run(task_path, out_path):
    with open(task_path) as f:
        task = json.load(f)
    trace = {'steps': []}
    for screen in task['screens']:
        step = process_screen(screen)
        trace['steps'].append(step)
    with open(out_path, 'w') as f:
        json.dump(trace, f, indent=2)
    print(f"Trace saved to {out_path}")

if __name__ == '__main__':
    # Usage: python run_benchmark.py tasks/example_task.json output/example_trace.json
    if len(sys.argv) != 3:
        print("Usage: python run_benchmark.py [task_path] [out_path]")
        exit(1)
    run(sys.argv[1], sys.argv[2])