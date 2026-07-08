# aetna-research-lab
Reference RBST logging and scoring harness for agent memory retrieval audits: boundary, provenance, latency, and outcome.
## Article
Boundary Failures, Not Storage: A Retrieval Stress-Test for Safe Agent Memory in Live Workflows
Agent memory safety is best benchmarked by live audits of each retrieval event, logging provenance, latency, and boundary scope, not by aggregate storage or recall rates.
## Purpose
This Article proposes the Retrieval Boundary Stress Test (RBST) protocol for benchmarking agent memory safety via per-retrieval audits; a minimal reference implementation (logging harness + analysis) makes the Article’s claims concrete, credible, and testable for the reader.
## Generated Notes
Reference RBST logging and scoring harness for agent memory retrieval audits: boundary, provenance, latency, and outcome.
## Article
Boundary Failures, Not Storage: A Retrieval Stress-Test for Safe Agent Memory in Live Workflows
Agent memory safety is best benchmarked by live audits of each retrieval event, logging provenance, latency, and boundary scope, not by aggregate storage or recall rates.
## Purpose
This Article proposes the Retrieval Boundary Stress Test (RBST) protocol for benchmarking agent memory safety via per-retrieval audits; a minimal reference implementation (logging harness + analysis) makes the Article’s claims concrete, credible, and testable for the reader.
## Generated Notes
A reference logging and scoring harness for memory safety in product AI agents. RBST benchmarks per-retrieval boundary, provenance, latency, and outcome (HIT, MISS, CROSS) for memory retrievals in agent workflows.

## What Is RBST?
RBST challenges agent stacks not by aggregate recall, but by logging every retrieval event and comparing it to declared boundaries, provenance, and expected workflow behavior, supporting root-cause audits of memory safety and trust failures.

- **Boundary:** Did retrieval respect the user/session/workflow/screen it claimed?
- **Provenance:** What was the real-world or workflow source of the retrieved item?
- **Latency:** Was the recall timely for real workflow pace?

Inspired by: [MemGPT](https://arxiv.org/abs/2310.08560), [Lost in the Middle](https://arxiv.org/abs/2307.03172), [RAG](https://arxiv.org/abs/2005.11401), [AgentBench](https://arxiv.org/abs/2308.03688), [Ragas](https://arxiv.org/abs/2309.15217)

## Usage

1. Instrument your agent stack with the provided `RBSTLogger` at every memory retrieval event.
2. Define adversarial test workflows with expected ground-truth boundaries and outcomes.
3. Log real/simulated retrievals as your agent acts.
4. Run the included scoring script to tally HIT, MISS, and CROSS events by retrieval, boundary, and provenance.

See [`rbst_logger.py`](rbst_logger.py) and [`score_rbst.py`](score_rbst.py) for details.

## Example Log Entry
```
{
  "step_id": 3, "query": "Recall user email for onboarding message", "intended_boundary": "user-501-session-abc", "provenance": "user-db-v4/email", "timestamp": "2024-06-08T14:02:21.034Z", "latency_ms": 34, "outcome": "HIT"
}
```

## Limitations
- No agent code, this is a test/logging harness, not a full agent.
- No privacy/PII redactions: use with synthetic, anonymized, or simulated data.
- Manual annotation of ground truth expected per workflow.

## License
MIT (for demo/benchmark use only)
## Files
- `README.md`: Explains what RBST is, design philosophy, how to instrument an agent stack, and outlines demo usage.
- `rbst_logger.py`: Provides the RBSTLogger class to be called at every agent memory retrieval event, encapsulating all logging schema per Article protocol.
- `score_rbst.py`: Scoring script to parse an RBST log, compute counts/rates of HIT/MISS/CROSS, and report median/mean latency.
- `example_workflow_fixture.jsonl`: Shows a minimal, annotated log file with different outcomes for test/demo purposes.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Explains what RBST is, design philosophy, how to instrument an agent stack, and outlines demo usage.
- `rbst_logger.py`: Provides the RBSTLogger class to be called at every agent memory retrieval event, encapsulating all logging schema per Article protocol.
- `score_rbst.py`: Scoring script to parse an RBST log, compute counts/rates of HIT/MISS/CROSS, and report median/mean latency.
- `example_workflow_fixture.jsonl`: Shows a minimal, annotated log file with different outcomes for test/demo purposes.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.