import json
import sys
from typing import List, Dict


def score_boundaries(steps: List[Dict]) -> Dict:
    """
    Scores boundary failures for each agent step and returns aggregated counts
    and a final success flag (only if no failures).
    """
    failures = {
        "missing_evidence": 0,
        "stale_state": 0,
        "ambiguous_intent": 0,
        "permission_gap": 0,
        "unverifiable_outcome": 0,
        "over_broad_memory": 0,
    }

    for step in steps:
        evidence_type = step.get("evidence_type")
        proposed_action = step.get("proposed_action")
        permission_boundary = step.get("permission_boundary")
        post_action_state = step.get("post_action_state")

        # Rule-based scoring (simplified)
        if not evidence_type or evidence_type not in [
            "observation", "inference", "preference", "instruction",
            "permission", "outcome"
        ]:
            failures["missing_evidence"] += 1
        if not post_action_state:
            failures["stale_state"] += 1
        if not proposed_action:
            failures["ambiguous_intent"] += 1
        if not permission_boundary:
            failures["permission_gap"] += 1
        if not post_action_state:
            failures["unverifiable_outcome"] += 1

        # Placeholder for over-broad memory detection
        # In a real implementation, compare memory/state access scope vs needed
        if "memory" in step.get("evidence_source", "") and len(step.get("evidence_source", "")) > 100:
            failures["over_broad_memory"] += 1

    total_failures = sum(failures.values())
    final_success = total_failures == 0

    return {
        "boundary_failures": failures,
        "total_failures": total_failures,
        "final_success": final_success
    }


def main():
    if len(sys.argv) != 2:
        print("Usage: python audit_card.py <input.json>")
        sys.exit(1)

    with open(sys.argv[1], "r") as f:
        steps = json.load(f)

    results = score_boundaries(steps)
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()