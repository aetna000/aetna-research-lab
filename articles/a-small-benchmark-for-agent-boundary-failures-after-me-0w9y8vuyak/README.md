# aetna-research-lab
Minimal code for logging and scoring workflow boundary steps in agent evaluations, a research harness for the 'audit card' method.
## Article
A Small Benchmark for Agent Boundary Failures After MemGPT: Towards LLMs as Operating S...
The product bottleneck for workflow benchmarks and evaluation design is not only model capability; it is whether each boundary in the agent step can be audited.
## Purpose
The Article advocates for an auditable agent step-by-step evaluation harness ('audit card') as the missing product standard. Supplying a minimal, reusable Python reference for logging, scoring, and inspecting workflow boundary events directly supports the thesis, provides a concrete product path, and distinguishes the Article from generic essays.
## Generated Notes
Minimal code for logging and scoring workflow boundary steps in agent evaluations, a research harness for the 'audit card' method.
## Article
A Small Benchmark for Agent Boundary Failures After MemGPT: Towards LLMs as Operating S...
The product bottleneck for workflow benchmarks and evaluation design is not only model capability; it is whether each boundary in the agent step can be audited.
## Purpose
The Article advocates for an auditable agent step-by-step evaluation harness ('audit card') as the missing product standard. Supplying a minimal, reusable Python reference for logging, scoring, and inspecting workflow boundary events directly supports the thesis, provides a concrete product path, and distinguishes the Article from generic essays.
## Generated Notes
This repo provides minimal code for the 'audit card' method proposed in [A Small Benchmark for Agent Boundary Failures After MemGPT](https://arxiv.org/abs/2310.08560).

## What is the Audit Card?
Audit cards record what an agent saw, inferred, remembered, was permitted to do, and what changed, at every workflow step. The idea is to create inspectable log objects for product or research teams to score boundary failures, rather than only tracking final success.

## What This Repo Provides
- A Python class for constructing and logging audit cards per agent step
- Utilities to score boundary failures (evidence, memory, permission, action, outcome)
- Example fixture logs and code for benchmarking or manual review

**No keys, API calls, or non-local dependencies required.**

## Why does this matter?
Most agent benchmarks report only task success. Serious product evaluation needs to catch where evidence-inference-action boundaries break, which is what this reference is for.

*References:*
- Article: A Small Benchmark for Agent Boundary Failures After MemGPT ([arxiv](https://arxiv.org/abs/2310.08560))
- MemGPT: [arxiv:2310.08560](https://arxiv.org/abs/2310.08560)
- Lost in the Middle: [arxiv:2307.03172](https://arxiv.org/abs/2307.03172)
## Files
- `README.md`: Explains why the repo exists, what it implements, and how a reader can use or extend it for workflow agent boundary evaluation.
- `audit_card.py`: Defines the AuditCard data structure, logging, replay, and a simple scoring function to surface boundary failures.
- `example_fixture.py`: Gives an inspectable example of logging agent workflow steps and scoring boundary failures.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Explains why the repo exists, what it implements, and how a reader can use or extend it for workflow agent boundary evaluation.
- `audit_card.py`: Defines the AuditCard data structure, logging, replay, and a simple scoring function to surface boundary failures.
- `example_fixture.py`: Gives an inspectable example of logging agent workflow steps and scoring boundary failures.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.