# aetna-research-lab
Minimal boundary-audit card protocol and scorer for workflow agent evaluation. Supports evidence, inference, memory, permission, and outcome tracking.
## Article
A Small Benchmark for Agent Boundary Failures After MemGPT: Towards LLMs as Operating S...
The product bottleneck for workflow benchmarks and evaluation design is not only model capability; it is whether each boundary in the agent step can be audited.
## Purpose
The article’s thesis is that workflow agent evaluation should be based on boundary-level, inspectable audit objects, not just aggregate task scores. A public, minimal implementation of the 'workflow audit card' concept enables reproducibility, grounds the article’s claims, and lets researchers, agent builders, or reviewers see the exact mechanics of boundary failure annotation. This directly supports transparency and productization for memory-safety benchmarking.
## Generated Notes
Minimal boundary-audit card protocol and scorer for workflow agent evaluation. Supports evidence, inference, memory, permission, and outcome tracking.
## Article
A Small Benchmark for Agent Boundary Failures After MemGPT: Towards LLMs as Operating S...
The product bottleneck for workflow benchmarks and evaluation design is not only model capability; it is whether each boundary in the agent step can be audited.
## Purpose
The article’s thesis is that workflow agent evaluation should be based on boundary-level, inspectable audit objects, not just aggregate task scores. A public, minimal implementation of the 'workflow audit card' concept enables reproducibility, grounds the article’s claims, and lets researchers, agent builders, or reviewers see the exact mechanics of boundary failure annotation. This directly supports transparency and productization for memory-safety benchmarking.
## Generated Notes
A minimal Python toolkit for recording, inspecting, and scoring agent steps where memory, evidence, intent, permission, and outcome boundaries can fail. Use as a reference for workflow benchmark traces and audit-driven agent evaluation.

## What is this?
This tool logs each agent step as a structured audit card with annotations for boundary evidence, inference, state, action, and post-action verification.

## Why?
It implements the audit card protocol proposed in [A Small Benchmark for Agent Boundary Failures After MemGPT](https://arxiv.org/abs/2310.08560) and related research, supporting open discussion and reproducible agent evaluation.

## How?
- Fill an AuditCard for each agent step using the Python class or YAML/JSON schema.
- Use `AuditScorer` to compute step and workflow-level boundary failure metrics.
- Review which boundary (evidence, inference, memory, permission, action, outcome) failed or needs human inspection.

## Example
See `example_audit_trace.py` for a minimal boundary audit and scoring demo.
## Files
- `README.md`: Explains how to use, extend, and inspect the audit card tool and what the scoring protocol evaluates.
- `audit_card.py`: Core data structures and logic for the AuditCard and AuditScorer classes supporting boundary annotation, storage, and scoring.
- `example_audit_trace.py`: Shows how to instantiate, populate, and score a workflow with several agent steps, including a boundary failure.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Explains how to use, extend, and inspect the audit card tool and what the scoring protocol evaluates.
- `audit_card.py`: Core data structures and logic for the AuditCard and AuditScorer classes supporting boundary annotation, storage, and scoring.
- `example_audit_trace.py`: Shows how to instantiate, populate, and score a workflow with several agent steps, including a boundary failure.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.