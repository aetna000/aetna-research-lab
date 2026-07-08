import json
import time
import argparse
from lrpa_schema import policy_check, make_event_log


def load_scenario(path):
    with open(path, 'r') as f:
        return json.load(f)

def run_lrpa_scenario(scenario_path, out_log_path):
    scenario = load_scenario(scenario_path)
    logs = []
    for step in scenario['steps']:
        retrieval = step['retrieval']
        t0 = time.time()
        outcome_obj = policy_check(retrieval)
        latency = time.time() - t0
        log_entry = make_event_log(retrieval, outcome_obj, latency)
        logs.append(log_entry)
    with open(out_log_path, 'w') as f:
        json.dump(logs, f, indent=2)
    print(f"LRPA audit log written to {out_log_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run LRPA scenario benchmark')
    parser.add_argument('--scenario', type=str, required=True, help='Input scenario JSON file (see fixtures)')
    parser.add_argument('--log', type=str, default='logs/lrpa_audit_log.json', help='Output log path')
    args = parser.parse_args()
    run_lrpa_scenario(args.scenario, args.log)