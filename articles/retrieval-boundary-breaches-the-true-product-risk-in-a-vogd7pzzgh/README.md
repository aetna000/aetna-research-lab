# aetna-research-lab
Reference code for the Retrieval Boundary Audit (RBA) protocol: agent memory logging, boundary/error scoring, and reproducible workflow benchmarking.
## Article
Retrieval Boundary Breaches: The True Product Risk in Agent Memory (And How To Benchmark It)
Memory safety in product AI agents is defined by the fidelity and boundary of retrieval events, not by aggregate storage, and must be benchmarked by per-retrieval provenance and boundary adherence.
## Purpose
The Article proposes a novel Retrieval Boundary Audit (RBA) benchmark and protocol, including a logging schema, scoring rubric, and example workflow traces for agent memory safety. Providing a reference implementation (Python logging harness, schema, and scoring script) makes the Article credible, actionable, and directly useful for researchers or product teams benchmarking agent memory in the wild.
## Generated Notes
Reference code for the Retrieval Boundary Audit (RBA) protocol: agent memory logging, boundary/error scoring, and reproducible workflow benchmarking.
## Article
Retrieval Boundary Breaches: The True Product Risk in Agent Memory (And How To Benchmark It)
Memory safety in product AI agents is defined by the fidelity and boundary of retrieval events, not by aggregate storage, and must be benchmarked by per-retrieval provenance and boundary adherence.
## Purpose
The Article proposes a novel Retrieval Boundary Audit (RBA) benchmark and protocol, including a logging schema, scoring rubric, and example workflow traces for agent memory safety. Providing a reference implementation (Python logging harness, schema, and scoring script) makes the Article credible, actionable, and directly useful for researchers or product teams benchmarking agent memory in the wild.
## Generated Notes
Reference code for the RBA benchmark protocol introduced in "Retrieval Boundary Breaches: The True Product Risk in Agent Memory (And How To Benchmark It)" by @aetna000.

This repo includes:
- A logging schema for agent memory retrieval events (JSONL)
- A Python logger (RBA harness) to capture per-retrieval events
- A scoring script for classifying and evaluating retrieval boundary errors
- Example input dataset and outputs

## Why RBA?
Agent memory safety must be measured at the retrieval boundary: per-retrieval fidelity, provenance, and scope, not just storage/recall rates.

See the Article for context: [Citation](https://arxiv.org/abs/2308.03688) / [repo]

## Getting Started

1. **Clone this repo**
2. **Install (Python 3.8+)**: No external requirements
3. **Run Example**:
    ```shell
    python rba_logger.py --logfile example_rba_log.jsonl
    python rba_score.py --input example_rba_log.jsonl
    ```

## Files
- `rba_schema.py`: Defines the JSONL event schema
- `rba_logger.py`: Minimal logger to emit per-retrieval events (can wrap agent workflows)
- `rba_score.py`: Evaluates RBA logs against the scoring rubric
- `example_rba_log.jsonl`: Sample annotated trace

## Article
"Retrieval Boundary Breaches: The True Product Risk in Agent Memory (And How To Benchmark It)"
(Cites: AgentBench, MemGPT, Ragas, 'Lost in the Middle')
## Files
- `README.md`: Repo overview, install/run instructions, Article reference, and usage example for RBA logging and scoring.
- `rba_schema.py`: Defines and validates the RBA JSONL event schema for agent memory retrievals.
- `rba_logger.py`: Python script to log per-memory retrieval events conforming to the RBA schema.
- `rba_score.py`: Implements the Article's scoring rubric for RBA logs: per-event score, aggregate error/latency/rate stats.
- `example_rba_log.jsonl`: Minimal example input (3 events) for RBA logger and scoring, reflecting a typical product use case.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Repo overview, install/run instructions, Article reference, and usage example for RBA logging and scoring.
- `rba_schema.py`: Defines and validates the RBA JSONL event schema for agent memory retrievals.
- `rba_logger.py`: Python script to log per-memory retrieval events conforming to the RBA schema.
- `rba_score.py`: Implements the Article's scoring rubric for RBA logs: per-event score, aggregate error/latency/rate stats.
- `example_rba_log.jsonl`: Minimal example input (3 events) for RBA logger and scoring, reflecting a typical product use case.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.