# aetna-research-lab
Prototype code and schema for the Retrieval Boundary Audit (RBA): per-step agent memory retrieval logging, provenance, and boundary scoring.
## Article
How Safe Is Agent Memory? A Retrieval-Focused Benchmark for Boundary Failures and Provenance Gaps
Trustworthy AI agents must be benchmarked by the accuracy, provenance, boundary, and latency of every memory retrieval, not by storage claims or aggregate recall.
## Purpose
The Article proposes the Retrieval Boundary Audit (RBA) protocol for benchmarking agent memory safety via per-retrieval, provenance-tagged logs and boundary scoring. A minimal, open, reference implementation makes the benchmark reproducible, inspectable, and credible for X readers, fulfilling the mission to move past theory to testable artifact.
## Generated Notes
Prototype code and schema for the Retrieval Boundary Audit (RBA): per-step agent memory retrieval logging, provenance, and boundary scoring.
## Article
How Safe Is Agent Memory? A Retrieval-Focused Benchmark for Boundary Failures and Provenance Gaps
Trustworthy AI agents must be benchmarked by the accuracy, provenance, boundary, and latency of every memory retrieval, not by storage claims or aggregate recall.
## Purpose
The Article proposes the Retrieval Boundary Audit (RBA) protocol for benchmarking agent memory safety via per-retrieval, provenance-tagged logs and boundary scoring. A minimal, open, reference implementation makes the benchmark reproducible, inspectable, and credible for X readers, fulfilling the mission to move past theory to testable artifact.
## Generated Notes
This repo is a minimal prototype for the Retrieval Boundary Audit (RBA) protocol as described in the Article:

**How Safe Is Agent Memory? A Retrieval-Focused Benchmark for Boundary Failures and Provenance Gaps.**

## What is RBA?
RBA is a benchmark for product AI agents: it logs every agent memory retrieval, attaches scope and provenance, and scores per retrieval for fidelity, boundary, and latency.

## What is in this repo?
- A JSON schema for per-retrieval event logs
- A Python script to compute RBA scores given a log
- Example event logs and outputs

## References
- Article: [How Safe Is Agent Memory?](https://twitter.com/aetna000/status/...) (link to X Article)
- MemGPT: https://arxiv.org/abs/2310.08560
- Lost in the Middle: https://arxiv.org/abs/2307.03172

## Usage
Inspect the example log, then run:

```bash
python score_rba.py example_rba_log.json
```

Outputs a per-retrieval and aggregate score table.
## Files
- `README.md`: Explain what RBA is, how to use the prototype, and reference the Article.
- `rba_event_schema.json`: Defines the per-retrieval event log schema, supporting reproducible scoring and provenance-attached evaluation.
- `score_rba.py`: Scoring script for RBA event logs. Implements protocol rules for +1/0/-1 scoring by outcome, aggregates results.
- `example_rba_log.json`: Give a toy RBA event log with different retrieval outcomes for example scoring.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Explain what RBA is, how to use the prototype, and reference the Article.
- `rba_event_schema.json`: Defines the per-retrieval event log schema, supporting reproducible scoring and provenance-attached evaluation.
- `score_rba.py`: Scoring script for RBA event logs. Implements protocol rules for +1/0/-1 scoring by outcome, aggregates results.
- `example_rba_log.json`: Give a toy RBA event log with different retrieval outcomes for example scoring.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.