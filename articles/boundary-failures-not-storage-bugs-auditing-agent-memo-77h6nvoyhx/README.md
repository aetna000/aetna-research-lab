# aetna-research-lab
Prototype harness for logging and scoring agent memory retrieval events with boundary/provenance audits as proposed by Aetna's Retrieval Boundary Audit.
## Article
Boundary Failures, Not Storage Bugs: Auditing Agent Memory with Retrieval-Focused Benchmarks
Agent memory safety in product workflows is defined not by aggregate storage, but by live, provenance-logged boundary adherence at each retrieval event; retrieval must be measured, logged, and tested per boundary to secure agent trust.
## Purpose
The Article's core claim is operational: memory safety must be benchmarked by live retrieval boundary audits, not aggregate recall. A minimal public code artifact makes this credible, showing how to log, score, and validate retrieval events with boundaries and provenance, which is missing from current public agent repos.
## Generated Notes
Prototype harness for logging and scoring agent memory retrieval events with boundary/provenance audits as proposed by Aetna's Retrieval Boundary Audit.
## Article
Boundary Failures, Not Storage Bugs: Auditing Agent Memory with Retrieval-Focused Benchmarks
Agent memory safety in product workflows is defined not by aggregate storage, but by live, provenance-logged boundary adherence at each retrieval event; retrieval must be measured, logged, and tested per boundary to secure agent trust.
## Purpose
The Article's core claim is operational: memory safety must be benchmarked by live retrieval boundary audits, not aggregate recall. A minimal public code artifact makes this credible, showing how to log, score, and validate retrieval events with boundaries and provenance, which is missing from current public agent repos.
## Generated Notes
A prototype harness for logging and scoring agent memory retrievals with boundary and provenance audits, as proposed in [Boundary Failures, Not Storage Bugs: Auditing Agent Memory with Retrieval-Focused Benchmarks].

## Purpose

- Log every agent memory retrieval event with declared boundary and provenance.
- Score events for boundary-adherence, provenance and latency.
- Serve as a testable reference implementation for benchmarking agent memory safety, aligned with Aetna's Retrieval Boundary Audit (RBA) protocol.

For reproducibility and safety: no real user data, no secrets or keys, no API dependencies.

## Quickstart

1. Clone repo
2. Run `python audit_example.py` to simulate agent retrieval events and print scores.
3. Inspect/edit `audit_scoring.py` for core logic and scoring rubric.

## File Overview
- `audit_logging.py`: Defines retrieval event and logging utilities.
- `audit_scoring.py`: Implements the scoring protocol per event and aggregates results.
- `audit_example.py`: Simulates an example agent workflow with correct and boundary-violating retrievals.

## Referenced By
_Aetna, 2024. "Boundary Failures, Not Storage Bugs: Auditing Agent Memory with Retrieval-Focused Benchmarks."_
## Files
- `README.md`: Describes purpose, quickstart, and Article context; explains boundary audit concept and main CLI usage.
- `audit_logging.py`: Defines the data structures and logger for retrieval events, including boundary, provenance, and step context.
- `audit_scoring.py`: Implements the RBA scoring protocol: per-event and aggregate scores, latency break, and error detection.
- `audit_example.py`: Simulates a minimal agent workflow: correct retrieval, cross-boundary retrieval, high-latency retrieval, logs and scores events.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Describes purpose, quickstart, and Article context; explains boundary audit concept and main CLI usage.
- `audit_logging.py`: Defines the data structures and logger for retrieval events, including boundary, provenance, and step context.
- `audit_scoring.py`: Implements the RBA scoring protocol: per-event and aggregate scores, latency break, and error detection.
- `audit_example.py`: Simulates a minimal agent workflow: correct retrieval, cross-boundary retrieval, high-latency retrieval, logs and scores events.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.