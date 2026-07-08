# aetna-research-lab
Reference code for Workflow-Oriented Retrieval Boundary Audit (WORBA): benchmark harness, schema, and example for auditing agent memory safety.
## Article
Beyond Storage: Benchmarking Agent Memory Safety with Live Retrieval Boundary Stress-Tests
The defining product benchmark for agent memory safety is not storage or recall rate, it is adversarial, timestamped retrieval audits that expose boundary leaks, provenance confusion, and recall latency under real workflow pressure.
## Purpose
The article proposes WORBA, a concrete protocol for benchmarking agent memory safety via per-step, adversarial retrieval audits. Public code (even a minimal harness and schema) substantiates the novel benchmark and enables community adoption, reproducibility, and critique.
## Generated Notes
Reference code for Workflow-Oriented Retrieval Boundary Audit (WORBA): benchmark harness, schema, and example for auditing agent memory safety.
## Article
Beyond Storage: Benchmarking Agent Memory Safety with Live Retrieval Boundary Stress-Tests
The defining product benchmark for agent memory safety is not storage or recall rate, it is adversarial, timestamped retrieval audits that expose boundary leaks, provenance confusion, and recall latency under real workflow pressure.
## Purpose
The article proposes WORBA, a concrete protocol for benchmarking agent memory safety via per-step, adversarial retrieval audits. Public code (even a minimal harness and schema) substantiates the novel benchmark and enables community adoption, reproducibility, and critique.
## Generated Notes
This repository provides a minimal, public benchmark harness and schema for the WORBA protocol, as introduced in the Article "Beyond Storage: Benchmarking Agent Memory Safety with Live Retrieval Boundary Stress-Tests."

## What is WORBA?
WORBA is a stepwise, adversarial agent memory audit: At every workflow/UI step, the harness injects retrieval probes (in-scope, out-of-scope, ambiguous), records timestamps, provenance, boundary match, leak/miss flags, and outputs a per-step audit log.

## Why?
Product agents must demonstrate memory safety live, not mere context size. WORBA shows where agents retrieve the wrong memory, slow down, or cross user/session/tool boundaries.

## What's here?
- `worba_schema.py`: Data schema for audit logs, boundary checks, and retrieval events.
- `worba_harness.py`: Minimal simulation of agent steps, retrievals, boundary probes, and scoring.
- `examples/example_audit_run.py`: Concrete audit trace for a 3-step multi-user workflow (with comments).

### Limitations
- This reference harness is not a replacement for in-stack production instrumentation.
- Synthetic agents and memory stores here are for demonstration, real systems must log and prove actual provenance.
- No results are benchmarked on live agent frameworks yet.

## References
- [Article: Beyond Storage: Benchmarking Agent Memory Safety with Live Retrieval Boundary Stress-Tests](URL_PLACEHOLDER)
- MemGPT: https://arxiv.org/abs/2310.08560
- RAG: https://arxiv.org/abs/2005.11401
- Ragas: https://arxiv.org/abs/2309.15217
- AgentBench: https://arxiv.org/abs/2308.03688
## Files
- `README.md`: Explain the WORBA protocol, repo purpose, example usage, and limitations.
- `worba_schema.py`: Defines Python dataclasses for retrieval audit events, provenance, boundary match, and per-step audit results (WORBA schema).
- `worba_harness.py`: Minimal simulation harness for running WORBA audits on a synthetic, in-memory agent and memory store. Handles test workflow, adversarial probes, and outputs AuditRun.
- `examples/example_audit_run.py`: Script to run a sample WORBA audit on the synthetic harness and print the results. Enables quick reproduction of audit traces.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Explain the WORBA protocol, repo purpose, example usage, and limitations.
- `worba_schema.py`: Defines Python dataclasses for retrieval audit events, provenance, boundary match, and per-step audit results (WORBA schema).
- `worba_harness.py`: Minimal simulation harness for running WORBA audits on a synthetic, in-memory agent and memory store. Handles test workflow, adversarial probes, and outputs AuditRun.
- `examples/example_audit_run.py`: Script to run a sample WORBA audit on the synthetic harness and print the results. Enables quick reproduction of audit traces.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.