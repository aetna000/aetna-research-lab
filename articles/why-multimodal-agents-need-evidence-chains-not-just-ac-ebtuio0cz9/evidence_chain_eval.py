#!/usr/bin/env python3
"""Minimal evidence-chain evaluator for multimodal agent action traces."""

import json
import sys


REQUIRED_FIELDS = [
    "pre_action_screen_state",
    "visible_evidence",
    "inferred_user_intent",
    "selected_action",
    "post_action_state",
    "observed_outcome",
]


def score_trace(trace):
    present = [field for field in REQUIRED_FIELDS if trace.get(field)]
    missing = [field for field in REQUIRED_FIELDS if not trace.get(field)]
    evidence_links = trace.get("evidence_links", []) or []
    score = round((len(present) / len(REQUIRED_FIELDS)) * 70 + min(len(evidence_links), 3) * 10)
    return {
        "score": min(score, 100),
        "present": present,
        "missing": missing,
        "evidence_link_count": len(evidence_links),
        "interpretation": interpret(score, missing),
    }


def interpret(score, missing):
    if missing:
        return "incomplete evidence chain"
    if score >= 90:
        return "strong trace, still needs human review"
    return "usable trace, but evidence links are thin"


def main(path):
    with open(path, "r", encoding="utf-8") as handle:
        trace = json.load(handle)
    print(json.dumps(score_trace(trace), indent=2))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: python3 evidence_chain_eval.py examples/sample_trace.json")
    main(sys.argv[1])