# aetna-research-lab
Reference implementation of the Omission Audit Benchmark (OAB) for scoring agent memory omission errors.
## Article
Beyond Boundaries: Memory Omission Failures in Agents and the Omission Audit Benchmark
Silent omission, when an agent fails to retrieve necessary context, is the most dangerous and least measured memory failure: only an omission audit benchmark can reveal or reduce it.
## Purpose
The article defines a new benchmark protocol (OAB). A minimal reference implementation of the scoring harness and an example annotated workflow makes the audit concrete, reproducible, and ready for adaptation by agent engineers.
## Generated Notes
Reference implementation of the Omission Audit Benchmark (OAB) for scoring agent memory omission errors.
## Article
Beyond Boundaries: Memory Omission Failures in Agents and the Omission Audit Benchmark
Silent omission, when an agent fails to retrieve necessary context, is the most dangerous and least measured memory failure: only an omission audit benchmark can reveal or reduce it.
## Purpose
The article defines a new benchmark protocol (OAB). A minimal reference implementation of the scoring harness and an example annotated workflow makes the audit concrete, reproducible, and ready for adaptation by agent engineers.
## Generated Notes
This repository provides a minimal reference implementation of the Omission Audit Benchmark introduced in the article *Beyond Boundaries: Memory Omission Failures in Agents and the Omission Audit Benchmark*.

The OAB scores agent memory omissions, required facts that should have been retrieved at a specific workflow step but were not. This harness takes a JSON log of agent retrievals and an annotated set of must‑recall facts, then computes:

- Omission rate
- Root‑cause breakdown (index miss, scoring error, context dropout, pipeline path miss)
- Workflow‑level error propagation

## Usage

1. Prepare a workflow log (see `example_workflow.json`).
2. Run the scorer:
   ```bash
   python oab_scorer.py example_workflow.json
   ```
3. The script outputs a markdown report to stdout.

## File Descriptions

- `oab_scorer.py`, Main scoring logic.
- `example_workflow.json`, Annotated example with five workflow steps.

## No Dependencies

Only requires Python 3.8+. No external packages.

## Disclaimer

This is a research prototype. Real‑world omission ground‑truth is expensive to annotate; this harness assumes a manually annotated workflow. It is intended to demonstrate the scoring algorithm and encourage extension.
## Files
- `README.md`: Explains what the OAB is, how to use the harness, and how it relates to the article.
- `oab_scorer.py`: Implements the OAB scoring procedure: loads a workflow log, checks omissions, computes metrics, prints report.
- `example_workflow.json`: An annotated workflow with five steps, each containing required facts and agent retrievals; demonstrates the OAB harness.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Explains what the OAB is, how to use the harness, and how it relates to the article.
- `oab_scorer.py`: Implements the OAB scoring procedure: loads a workflow log, checks omissions, computes metrics, prints report.
- `example_workflow.json`: An annotated workflow with five steps, each containing required facts and agent retrievals; demonstrates the OAB harness.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.