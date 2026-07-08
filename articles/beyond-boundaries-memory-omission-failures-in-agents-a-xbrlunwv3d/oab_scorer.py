#!/usr/bin/env python3
"""
Omission Audit Benchmark (OAB) Scoring Harness.

Reads a JSON workflow log with annotated must-recall facts and agent retrieval logs,
then computes omission rate, root-cause breakdown, and workflow-level impact.
"""
import json
import sys
from collections import Counter


def load_workflow(path):
    with open(path, 'r') as f:
        return json.load(f)


def check_omission(step):
    """
    For a single workflow step, check if each required fact appears in the
    agent's retrieved context set.
    Returns a list of omission records.
    """
    retrievals = {r['fact_id'] for r in step.get('retrieved_contexts', [])}
    omissions = []
    for required in step.get('required_facts', []):
        if required['fact_id'] not in retrievals:
            omissions.append({
                'fact_id': required['fact_id'],
                'description': required.get('description', ''),
                'root_cause': required.get('expected_root_cause', 'unknown'),
                'product_impact': required.get('product_impact', 'minor')
            })
    return omissions


def score_workflow(workflow):
    """
    Iterate over all steps, compute omission counts and root causes.
    Return a results dictionary.
    """
    total_required = 0
    total_omissions = 0
    root_cause_counter = Counter()
    step_reports = []

    for step in workflow.get('steps', []):
        omissions = check_omission(step)
        total_required += len(step.get('required_facts', []))
        total_omissions += len(omissions)
        for o in omissions:
            root_cause_counter[o['root_cause']] += 1

        step_reports.append({
            'step_id': step.get('step_id'),
            'required_facts': len(step.get('required_facts', [])),
            'omissions': len(omissions),
            'omission_details': omissions
        })

    omission_rate = total_omissions / total_required if total_required else 0.0
    return {
        'omission_rate': omission_rate,
        'total_required_facts': total_required,
        'total_omissions': total_omissions,
        'root_cause_breakdown': dict(root_cause_counter),
        'step_reports': step_reports
    }


def print_report(results):
    print("# OAB Scoring Report")
    print(f"- Overall Omission Rate: {results['omission_rate']:.3f}")
    print(f"- Total Required Facts: {results['total_required_facts']}")
    print(f"- Total Omissions: {results['total_omissions']}")
    print("\n## Root‑Cause Breakdown")
    for cause, count in results['root_cause_breakdown'].items():
        print(f"- {cause}: {count}")
    print("\n## Per‑Step Summary")
    for step in results['step_reports']:
        print(f"- Step {step['step_id']}: {step['omissions']} omissions out of {step['required_facts']} required facts")
        for omit in step['omission_details']:
            print(f"  - {omit['fact_id']}: {omit['description']} (cause: {omit['root_cause']}, impact: {omit['product_impact']})")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python oab_scorer.py <workflow.json>")
        sys.exit(1)
    wf = load_workflow(sys.argv[1])
    results = score_workflow(wf)
    print_report(results)