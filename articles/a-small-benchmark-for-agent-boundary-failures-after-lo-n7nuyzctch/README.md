# aetna-research-lab
Minimal boundary-audit benchmark for agent workflow evidence, inference, permission, and outcome steps. Reference for agent memory safety evaluation.
## Article
A Small Benchmark for Agent Boundary Failures After Lost in the Middle: How Language Mo...
The product bottleneck for workflow benchmarks and evaluation design is not only model capability; it is whether each boundary in the agent step can be audited.
## Purpose
The Article's core claim is an actionable, testable audit card for agent workflow boundary evaluation. A minimal, inspectable, and reusable Python implementation is needed to make the benchmark concrete and credible. It allows researchers and product builders to understand, critique, and extend the workflow audit process using real or toy agent traces.
## Generated Notes
Minimal boundary-audit benchmark for agent workflow evidence, inference, permission, and outcome steps. Reference for agent memory safety evaluation.
## Article
A Small Benchmark for Agent Boundary Failures After Lost in the Middle: How Language Mo...
The product bottleneck for workflow benchmarks and evaluation design is not only model capability; it is whether each boundary in the agent step can be audited.
## Purpose
The Article's core claim is an actionable, testable audit card for agent workflow boundary evaluation. A minimal, inspectable, and reusable Python implementation is needed to make the benchmark concrete and credible. It allows researchers and product builders to understand, critique, and extend the workflow audit process using real or toy agent traces.
## Generated Notes
This repo implements the audit card and scoring logic from the Aetna research note on workflow benchmarks and evaluation design for product agents.

## What is this?
A boundary-audit harness for agent workflow steps: each agent action is logged as a structured event, recording observation, inference, memory read, permission, proposed action, outcome, and boundary audit scores.

It is minimal, no extraneous dependencies. Intended to be readable, extensible, and suitable for real or toy agent traces.

## How to Use
- Inspect or run `audit_card.py` as a standalone script.
- Provide a trace of agent steps (see `examples/`).
- The script will produce a JSONL log and summary boundary report.

## What does it test?
- Whether each agent action clearly exposes evidence, inference, memory, permission, action, and outcome.
- Boundary failures are flagged: missing evidence, ambiguous memory, permission gaps, or unverifiable outcomes.

## Why not use an existing benchmark?
Existing agent/test harnesses do not type-check evidence or permission boundary at every workflow step. This audit card fills the gap with a practical, inspectable protocol.

## Example
See `examples/trace_example.jsonl` for a sample agent workflow and boundary scores.
## Files
- `README.md`: Explain the boundary audit card, how to use the evaluation, and show an example agent step trace.
- `audit_card.py`: Core code to define the audit card schema, boundary scoring, and minimal workflow evaluation routine.
- `examples/trace_example.jsonl`: Provide a realistic example of a three-step agent workflow with at least one boundary failure.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Explain the boundary audit card, how to use the evaluation, and show an example agent step trace.
- `audit_card.py`: Core code to define the audit card schema, boundary scoring, and minimal workflow evaluation routine.
- `examples/trace_example.jsonl`: Provide a realistic example of a three-step agent workflow with at least one boundary failure.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.