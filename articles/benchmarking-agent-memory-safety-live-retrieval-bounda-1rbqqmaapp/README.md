# aetna-research-lab
Reference implementation of the Retrieval Boundary Audit (RBA) Protocol for scoring and benchmarking agent memory safety.
## Article
Benchmarking Agent Memory Safety: Live Retrieval Boundary Tests, Not Storage Claims
The product bottleneck for agent memory safety is not storage size but whether every retrieval is faithfully logged, boundary-checked, and provenance-attached at every workflow step.
## Purpose
A minimal reference implementation of the Retrieval Boundary Audit (RBA) protocol strengthens the article by turning the proposed benchmark into inspectable, runnable code, allowing researchers to see the logging format, scoring rubric, and sample events.
## Generated Notes
Reference implementation of the Retrieval Boundary Audit (RBA) Protocol for scoring and benchmarking agent memory safety.
## Article
Benchmarking Agent Memory Safety: Live Retrieval Boundary Tests, Not Storage Claims
The product bottleneck for agent memory safety is not storage size but whether every retrieval is faithfully logged, boundary-checked, and provenance-attached at every workflow step.
## Purpose
A minimal reference implementation of the Retrieval Boundary Audit (RBA) protocol strengthens the article by turning the proposed benchmark into inspectable, runnable code, allowing researchers to see the logging format, scoring rubric, and sample events.
## Generated Notes
This repository accompanies the article *"Benchmarking Agent Memory Safety: Live Retrieval Boundary Tests, Not Storage Claims"* by Aetna. It provides a minimal reference implementation of the Retrieval Boundary Audit (RBA) Protocol, a benchmark for auditing agent memory retrieval in product workflows.

## What is RBA?

The RBA protocol evaluates an AI agent’s memory safety by instrumenting and scoring **every retrieval event** during a workflow. Instead of measuring just storage size or aggregate recall, RBA logs:

- **query**, the retrieval trigger (natural or structured)
- **intended boundary**, user, session, screen/UI, tool
- **provenance**, source file, screen hash, user/session ID, workflow step ID, timestamp
- **outcome**, HIT, MISS, CROSS_BOUNDARY, OMISSION, ERROR
- **latency**, retrieval time in milliseconds

The protocol then calculates metrics like boundary error rate, provenance coverage, retrieval latency profile, and omission rate.

## Repository Contents

- `rba_protocol.py`, Core data structures and scoring logic.
- `example_events.json`, Sample retrieval events (both normal and adversarial).
- `run_example.py`, Script to load events, run the scorer, and print a report.

## Running the Example

```bash
python run_example.py
```

Requires Python 3.9+ (no external dependencies).

## Limitations

- This is a **research prototype**, not production instrumentation. Real agent stacks require hooks into their retrieval pipelines.
- The example dataset is synthetic and tiny. A real benchmark needs large, annotated adversarial workflows.
- No privacy or redaction logic is included, that remains an open challenge.

## License

This code is provided for educational and research purposes. See the main article for full context.
## Files
- `README.md`: Explain the RBA protocol, the repository contents, usage, and limitations.
- `rba_protocol.py`: Define RetrievalEvent data class and RBAScorer that computes boundary-error rate, provenance coverage, latency percentiles, and omission rate, and prints a report.
- `example_events.json`: Sample retrieval events demonstrating normal and adversarial cases to exercise the RBA scorer.
- `run_example.py`: Load the example events, instantiate the scorer, print the report, and demonstrate how to use the protocol.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Explain the RBA protocol, the repository contents, usage, and limitations.
- `rba_protocol.py`: Define RetrievalEvent data class and RBAScorer that computes boundary-error rate, provenance coverage, latency percentiles, and omission rate, and prints a report.
- `example_events.json`: Sample retrieval events demonstrating normal and adversarial cases to exercise the RBA scorer.
- `run_example.py`: Load the example events, instantiate the scorer, print the report, and demonstrate how to use the protocol.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.