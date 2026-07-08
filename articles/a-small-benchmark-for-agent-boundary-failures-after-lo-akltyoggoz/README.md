# aetna-research-lab
Minimal reference implementation of the workflow boundary audit card from the article, with example input.
## Article
A Small Benchmark for Agent Boundary Failures After Lost in the Middle: How Language Mo...
The product bottleneck for workflow benchmarks and evaluation design is not only model capability; it is whether each boundary in the agent step can be audited.
## Purpose
The article proposes a novel audit card methodology for agent workflow evaluation. A minimal reference implementation of the audit card algorithm as a Python script, with an example input, makes the conceptual proposal more concrete and reproducible, adding credibility for researchers and builders.
## Generated Notes
Minimal reference implementation of the workflow boundary audit card from the article, with example input.
## Article
A Small Benchmark for Agent Boundary Failures After Lost in the Middle: How Language Mo...
The product bottleneck for workflow benchmarks and evaluation design is not only model capability; it is whether each boundary in the agent step can be audited.
## Purpose
The article proposes a novel audit card methodology for agent workflow evaluation. A minimal reference implementation of the audit card algorithm as a Python script, with an example input, makes the conceptual proposal more concrete and reproducible, adding credibility for researchers and builders.
## Generated Notes
Reference implementation for the audit card proposed in:

> A Small Benchmark for Agent Boundary Failures After Lost in the Middle: How Language Models Use Long Contexts

## Overview

This script implements the boundary audit card algorithm:
1. For each workflow step, capture the claim, evidence, memory/state read, permission boundary, action, expected outcome, and post-action observation.
2. Score each step on boundary failures: missing evidence, stale state, ambiguous intent, permission gap, unverifiable outcome, or over-broad memory use.
3. Produce an audit trace that separates success/failure from boundary violations.

## Usage

```bash
python audit_card.py --input example.json
```

### Input Format

A JSON file with an array of workflow steps, each containing:
- `step_name`: descriptive name
- `claim`: agent's claim or inference
- `evidence`: object with source details
- `claim_type`: one of observation, inference, preference, instruction, permission, outcome
- `memory_state`: snapshot of memory or state used
- `permission_boundary`: allowed actions/permissions
- `action_proposed`: action the agent wants to take
- `expected_outcome`: expected effect
- `post_action_observation`: actual observed outcome

### Output

A JSON audit report with per-step boundary scores, failure flags, and a final success assessment.

## Example

See `example.json` for a sample input. Run the script to see the output.

## Dependencies

Python 3.6+ (standard library only).
## Files
- `README.md`: Explains the audit card concept and how to run the reference implementation.
- `audit_card.py`: Implements the audit card algorithm: loads a workflow trace, scores each step on boundary failures, and outputs an audit report.
- `example.json`: Example input with two workflow steps, demonstrating the expected format for the audit card.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Explains the audit card concept and how to run the reference implementation.
- `audit_card.py`: Implements the audit card algorithm: loads a workflow trace, scores each step on boundary failures, and outputs an audit report.
- `example.json`: Example input with two workflow steps, demonstrating the expected format for the audit card.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.