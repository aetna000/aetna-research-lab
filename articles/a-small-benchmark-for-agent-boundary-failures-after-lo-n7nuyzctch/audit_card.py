import json
from typing import List, Dict, Any

BOUNDARY_TYPES = ["observation", "inference", "memory", "permission", "action", "outcome"]
FAILURE_TYPES = ["missing_evidence", "stale_state", "ambiguous_intent", "permission_gap", "unverifiable_outcome", "overbroad_memory"]

def audit_step(step: Dict[str, Any]) -> Dict[str, Any]:
    """
    Takes one workflow step dict and returns a boundary audit result.
    Input keys: claim, evidence, evidence_type, state, permission, proposed_action, expected_outcome, post_action_state
    """
    result = {"step": step, "boundary_failures": [], "success": True}
    # 1. Evidence required for any inference or action
    if step.get("evidence") is None:
        result["boundary_failures"].append("missing_evidence")
    # 2. Permission for proposed action
    if step.get("proposed_action") and not step.get("permission"):
        result["boundary_failures"].append("permission_gap")
    # 3. Verify type matches (example: observation cannot trigger unsafe action)
    if step.get("evidence_type") == "observation" and step.get("proposed_action") in ("delete", "modify"):
        result["boundary_failures"].append("action_mismatch")
    # 4. Outcome must be verifiable (i.e., post_action_state must differ if action expected to change state)
    if step.get("expected_outcome") and step.get("expected_outcome") != step.get("post_action_state"):
        result["boundary_failures"].append("unverifiable_outcome")
    # More boundary rules can be added here
    result["success"] = len(result["boundary_failures"]) == 0
    return result

def audit_trace(trace: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [audit_step(step) for step in trace]

def print_report(trace_results: List[Dict[str, Any]]):
    print("Boundary Audit Report\n====================\n")
    for i, r in enumerate(trace_results):
        sf = r["success"]
        print(f"Step {i+1}: {'PASS' if sf else 'FAIL'}")
        if not sf:
            print(f"  Failures: {r['boundary_failures']}")
        print(f"  Claim: {r['step'].get('claim')}")
        print(f"  Evidence: {r['step'].get('evidence')}")
        print(f"  Action: {r['step'].get('proposed_action')}")
        print()
    n_fail = sum([not r["success"] for r in trace_results])
    print(f"Total steps: {len(trace_results)}. Steps with boundary failure: {n_fail}.")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--trace", type=str, required=True, help="Path to agent trace JSONL file.")
    args = parser.parse_args()
    trace = []
    with open(args.trace) as f:
        for line in f:
            trace.append(json.loads(line))
    results = audit_trace(trace)
    print_report(results)