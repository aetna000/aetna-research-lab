# aetna-research-lab
Reference schema and Python scorer for workflow agent boundary audit cards. Supports boundary-failure analysis as argued in Aetna's benchmark Article.
## Article
A Small Benchmark for Agent Boundary Failures After Lost in the Middle: How Language Mo...
The product bottleneck for workflow benchmarks and evaluation design is not only model capability; it is whether each boundary in the agent step can be audited.
## Purpose
The Article proposes a workflow agent audit card as the minimal missing product standard for memory safety evaluation, but without a concrete schema or sample implementation, the research is toothless. A small repo with an audit card schema, example, and scoring logic grounds the Article's claims and gives researchers/engineers a visible reference point for discussion and reproducibility.
## Generated Notes
Reference schema and Python scorer for workflow agent boundary audit cards. Supports boundary-failure analysis as argued in Aetna's benchmark Article.
## Article
A Small Benchmark for Agent Boundary Failures After Lost in the Middle: How Language Mo...
The product bottleneck for workflow benchmarks and evaluation design is not only model capability; it is whether each boundary in the agent step can be audited.
## Purpose
The Article proposes a workflow agent audit card as the minimal missing product standard for memory safety evaluation, but without a concrete schema or sample implementation, the research is toothless. A small repo with an audit card schema, example, and scoring logic grounds the Article's claims and gives researchers/engineers a visible reference point for discussion and reproducibility.
## Generated Notes
Implements the audit card schema and scoring demo for workflow agent step evaluation as proposed in the X Article:

"A Small Benchmark for Agent Boundary Failures After Lost in the Middle: How Language Models Use Long Contexts"

## Purpose
This repo provides:
- A JSON schema for agent 'audit cards' capturing evidence, memory, permission, action, and outcome for each step.
- A Python scorer to categorize boundary failures in workflow traces.
- An example workflow audit trace.

Source Article thesis: the value bottleneck for agent evaluation is not model accuracy, but the replayable audit of each evidence boundary. See [arxiv:2307.03172](https://arxiv.org/abs/2307.03172) and related sources.

## Usage
1. Inspect `audit_card_schema.json` for record format.
2. See `examples/sample_trace.json` for mock data.
3. Run `score_audit_trace.py` on a trace file to identify boundary failures.

_No real agent evaluation is performed. This is a research prototype for boundary-centered benchmark tooling._
## Files
- `README.md`: Documents the repo purpose, audit card schema, core usage, and Article context.
- `audit_card_schema.json`: Defines the audit card structure for scoring workflow agent steps.
- `score_audit_trace.py`: Scans a trace of audit cards for boundary failures and prints a summary.
- `examples/sample_trace.json`: Toy example to show what a boundary-audited agent workflow looks like.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Documents the repo purpose, audit card schema, core usage, and Article context.
- `audit_card_schema.json`: Defines the audit card structure for scoring workflow agent steps.
- `score_audit_trace.py`: Scans a trace of audit cards for boundary failures and prints a summary.
- `examples/sample_trace.json`: Toy example to show what a boundary-audited agent workflow looks like.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.