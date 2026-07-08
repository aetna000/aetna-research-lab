# aetna-research-lab
Minimal workflow audit card and boundary failure scorer for evaluating agent memory and evidence boundaries.
## Article
A Small Benchmark for Agent Boundary Failures After MemGPT: Towards LLMs as Operating S...
The product bottleneck for workflow benchmarks and evaluation design is not only model capability; it is whether each boundary in the agent step can be audited.
## Purpose
The article proposes a workflow audit card as the kernel of a benchmark for agent memory safety and evidence boundary inspection. A small code artifact makes the recommendation actionable and inspectable, helps product builders prototype audit logging for agent workflows, and supports the thesis that boundary failures are what must be measured. The code's scope is a minimal workflow audit card schema, boundary-failure scorer, and an example pipeline to demonstrate stepwise logging and replay.
## Generated Notes
Minimal workflow audit card and boundary failure scorer for evaluating agent memory and evidence boundaries.
## Article
A Small Benchmark for Agent Boundary Failures After MemGPT: Towards LLMs as Operating S...
The product bottleneck for workflow benchmarks and evaluation design is not only model capability; it is whether each boundary in the agent step can be audited.
## Purpose
The article proposes a workflow audit card as the kernel of a benchmark for agent memory safety and evidence boundary inspection. A small code artifact makes the recommendation actionable and inspectable, helps product builders prototype audit logging for agent workflows, and supports the thesis that boundary failures are what must be measured. The code's scope is a minimal workflow audit card schema, boundary-failure scorer, and an example pipeline to demonstrate stepwise logging and replay.
## Generated Notes
This repo provides a minimal, research-quality implementation of the workflow audit card and scoring procedure proposed in:

_A Small Benchmark for Agent Boundary Failures After MemGPT: Towards LLMs as Operating Systems_

## Purpose

- Define a compact audit card schema for agent steps in real product workflows
- Log user-visible claim, evidence, memory/state, permission, action, and outcome per step
- Score boundary failures: missing evidence, stale state, ambiguous intent, permission gap, unverifiable outcome, or over-broad memory use
- Provide a simple, inspectable, non-production Python implementation with example trace and boundary scoring output

## Files
- `audit_card.py`: Core audit card dataclass, scoring functions, and boundary error taxonomy.
- `example_trace.json`: Example agent step trace with boundary fields (observation, inference, permission, action, outcome).
- `score_audit_trace.py`: Script that loads a trace, runs boundary checks, prints a readable boundary score report.

## Example Use
```bash
python score_audit_trace.py example_trace.json
```

## Limitations
- Prototype only: recording and replay assumes all steps provided by test designer.
- No external dependencies required (Python 3.8+).
- For research and product workflow evaluation, not for production or compliance.
## Files
- `README.md`: Explains the rationale, method, schema, and usage for the workflow audit card and boundary scorer prototype.
- `audit_card.py`: Defines the AuditCard dataclass, boundary failure scoring logic, and error taxonomy as a minimal, importable module.
- `score_audit_trace.py`: Entry-point script: loads a trace in JSON format, runs the audit scoring, and prints results.
- `example_trace.json`: Fixture file: provides an example agent trace with intentionally ambiguous boundaries, used for scoring demo.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Explains the rationale, method, schema, and usage for the workflow audit card and boundary scorer prototype.
- `audit_card.py`: Defines the AuditCard dataclass, boundary failure scoring logic, and error taxonomy as a minimal, importable module.
- `score_audit_trace.py`: Entry-point script: loads a trace in JSON format, runs the audit scoring, and prints results.
- `example_trace.json`: Fixture file: provides an example agent trace with intentionally ambiguous boundaries, used for scoring demo.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.