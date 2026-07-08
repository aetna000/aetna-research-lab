# aetna-research-lab
Reference implementation of the Retrieval Boundary Audit (RBA) protocol for logging, scoring, and exporting agent memory retrieval traces.
## Article
Not What You Store, But When You Recall: Auditing Memory Safety with Retrieval Boundary Traces
Reliable agent memory is defined not by storage, but by whether every retrieval is timely, boundary-faithful, and attributable, measured via retrieval boundary audits, not bulk logs.
## Purpose
The article proposes a concrete protocol (Retrieval Boundary Audit) with step-by-step instrumentation and scoring. A small reference implementation makes the protocol inspectable and credible for researchers and builders who want to adopt or benchmark it.
## Generated Notes
Reference implementation of the Retrieval Boundary Audit (RBA) protocol for logging, scoring, and exporting agent memory retrieval traces.
## Article
Not What You Store, But When You Recall: Auditing Memory Safety with Retrieval Boundary Traces
Reliable agent memory is defined not by storage, but by whether every retrieval is timely, boundary-faithful, and attributable, measured via retrieval boundary audits, not bulk logs.
## Purpose
The article proposes a concrete protocol (Retrieval Boundary Audit) with step-by-step instrumentation and scoring. A small reference implementation makes the protocol inspectable and credible for researchers and builders who want to adopt or benchmark it.
## Generated Notes
Reference implementation of the Retrieval Boundary Audit protocol for agent memory safety.

## What is RBA?

RBA is a protocol for instrumenting, scoring, and benchmarking AI agent memory safety by focusing on **live retrieval fidelity, boundary enforcement, and latency**, not just storage or recall rate. It logs every memory retrieval query with provenance, outcome, and scope, then scores each workflow run along fidelity, boundary, and latency dimensions.

This repo provides:
- `rba.py`, core classes: `RetrievalEvent`, `AuditLog`, `AuditScorer`
- `example.py`, demonstration with a synthetic workflow

## Quickstart

```bash
python example.py
```

No external dependencies required (pure Python stdlib).

## Files

- `README.md`
- `rba.py`
- `example.py`

## License

MIT
## Files
- `README.md`: Project overview, installation, and quickstart.
- `rba.py`: Core RBA logging and scoring implementation.
- `example.py`: Demonstrates RBA protocol with a synthetic three-step workflow.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Project overview, installation, and quickstart.
- `rba.py`: Core RBA logging and scoring implementation.
- `example.py`: Demonstrates RBA protocol with a synthetic three-step workflow.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.