import json
import sys


def audit_workflow(steps: list) -> dict:
    boundary_checks = [
        {
            "name": "missing_evidence",
            "check": lambda s: not s.get("evidence") or not s["evidence"].get("source")
        },
        {
            "name": "stale_state",
            "check": lambda s: s.get("memory_state", {}).get("age_seconds", 0) > 300
        },
        {
            "name": "ambiguous_intent",
            "check": lambda s: s["claim_type"] not in ["observation", "inference", "preference",
                                                         "instruction", "permission", "outcome"]
        },
        {
            "name": "permission_gap",
            "check": lambda s: s.get("permission_boundary") and s["action_proposed"] not in s["permission_boundary"]
        },
        {
            "name": "unverifiable_outcome",
            "check": lambda s: not s.get("post_action_observation") or s["post_action_observation"].get("status") == "unknown"
        },
        {
            "name": "overbroad_memory",
            "check": lambda s: len(s.get("memory_state", {}).get("keys_accessed", [])) > 10
        }
    ]

    report = {
        "audit_results": []
    }

    for step in steps:
        step_report = {
            "step_name": step.get("step_name", ""),
            "boundary_failures": []
        }
        for check in boundary_checks:
            if check["check"](step):
                step_report["boundary_failures"].append(check["name"])
        step_report["success"] = not bool(step_report["boundary_failures"])
        report["audit_results"].append(step_report)

    report["overall_success"] = all(r["success"] for r in report["audit_results"])
    return report


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] != "--input":
        print("Usage: python audit_card.py --input <file.json>")
        sys.exit(1)

    input_file = sys.argv[2]
    try:
        with open(input_file) as f:
            steps = json.load(f)
    except Exception as e:
        print(f"Error reading input: {e}")
        sys.exit(1)

    if not isinstance(steps, list):
        print("Input must be a JSON array of workflow steps.")
        sys.exit(1)

    report = audit_workflow(steps)
    print(json.dumps(report, indent=2))