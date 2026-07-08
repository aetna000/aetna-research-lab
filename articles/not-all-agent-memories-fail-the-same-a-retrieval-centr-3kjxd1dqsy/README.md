# aetna-research-lab
Reference implementation of the Memory Retrieval Latency and Boundary Audit (MRLBA) protocol for benchmarking agent memory safety in real workflows.
## Article
Not All Agent Memories Fail the Same: A Retrieval-Centric Benchmark for Product-Grade AI Agents
The next product-standard benchmark for agent memory is retrieval-centered: to audit memory safety in real workflows, we must measure fidelity, latency, and boundary adherence of every memory access, not just what is stored or acted on.
## Purpose
The Article proposes a concrete benchmark protocol, the Memory Retrieval Latency and Boundary Audit (MRLBA). A minimal, inspectable reference implementation is necessary to make the methodology credible, allow peer review, and demonstrate how per-step retrieval boundary logging, latency measurement, and provenance annotation could be realized in real or synthetic agent workflows.
## Generated Notes
Reference implementation of the Memory Retrieval Latency and Boundary Audit (MRLBA) protocol for benchmarking agent memory safety in real workflows.
## Article
Not All Agent Memories Fail the Same: A Retrieval-Centric Benchmark for Product-Grade AI Agents
The next product-standard benchmark for agent memory is retrieval-centered: to audit memory safety in real workflows, we must measure fidelity, latency, and boundary adherence of every memory access, not just what is stored or acted on.
## Purpose
The Article proposes a concrete benchmark protocol, the Memory Retrieval Latency and Boundary Audit (MRLBA). A minimal, inspectable reference implementation is necessary to make the methodology credible, allow peer review, and demonstrate how per-step retrieval boundary logging, latency measurement, and provenance annotation could be realized in real or synthetic agent workflows.
## Generated Notes
Reference implementation for the Memory Retrieval Latency and Boundary Audit (MRLBA) protocol, as proposed in "Not All Agent Memories Fail the Same: A Retrieval-Centric Benchmark for Product-Grade AI Agents" ([X Article Reference](https://arxiv.org/abs/2308.03688)).

## Purpose

* Audit agent memory retrievals stepwise for boundary, latency, and provenance failures, not just storage or final output.
* Evaluate agent behavior in adversarial workflows with cross-session/user/memory traps.

## Why

Product-grade AI agents must not just store data safely, they must only retrieve what they are allowed, when needed, and always log provenance for each retrieval.

## Features
- Per-step retrieval logging schema
- Workflow runner for synthetic/adversarial agent tasks
- Automated scoring for boundary, latency, and provenance errors

## Quickstart

```bash
python3 mrlba_runner.py --trace demo_fixture.json
```

See `demo_fixture.json` for an example annotated workflow.

## Files
- `mrlba_schema.py`: Defines retrieval log schema and score functions.
- `mrlba_runner.py`: Runs the benchmark on workflow traces (real or synthetic).
- `demo_fixture.json`: Sample workflow with annotated retrievals (in-bounds, cross-boundary, stale).

## Citation
["Not All Agent Memories Fail the Same: A Retrieval-Centric Benchmark"](https://arxiv.org/abs/2308.03688)
## Files
- `README.md`: Documents the benchmark motivation, protocol overview, quickstart, example usage, and links to the X Article.
- `mrlba_schema.py`: Defines the Python data structures for the retrieval log entries, boundary labels, and scoring utilities for the benchmark.
- `mrlba_runner.py`: Runs and scores a workflow trace according to the retrieval-centric audit protocol, outputs per-step audit results.
- `demo_fixture.json`: Provides an example input workflow trace, with agent retrieval steps illustrating each boundary case audited by the protocol.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Documents the benchmark motivation, protocol overview, quickstart, example usage, and links to the X Article.
- `mrlba_schema.py`: Defines the Python data structures for the retrieval log entries, boundary labels, and scoring utilities for the benchmark.
- `mrlba_runner.py`: Runs and scores a workflow trace according to the retrieval-centric audit protocol, outputs per-step audit results.
- `demo_fixture.json`: Provides an example input workflow trace, with agent retrieval steps illustrating each boundary case audited by the protocol.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.