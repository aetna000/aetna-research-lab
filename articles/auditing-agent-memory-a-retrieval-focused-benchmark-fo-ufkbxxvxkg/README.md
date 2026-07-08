# aetna-research-lab
Reference code and dataset schema for the Retrieval Boundary Audit (RBA) benchmark: per-retrieval provenance, boundary, and latency logs for AI agent workflows.
## Article
Auditing Agent Memory: A Retrieval-Focused Benchmark for Real-World Workflow Safety
Memory safety in AI agents is defined at the boundary of retrieval: only a per-retrieval, provenance-logged audit can benchmark or enforce product-grade memory safety.
## Purpose
The Article introduces the Retrieval Boundary Audit (RBA) protocol as a stepwise, per-retrieval memory safety benchmark. A reference implementation is necessary: it directly supports the thesis by making RBA audits testable, reproducible, and inspectable by researchers and product builders. Standalone code to log, score, and export retrieval events substantiates the Article's claims.
## Generated Notes
Reference code and dataset schema for the Retrieval Boundary Audit (RBA) benchmark: per-retrieval provenance, boundary, and latency logs for AI agent workflows.
## Article
Auditing Agent Memory: A Retrieval-Focused Benchmark for Real-World Workflow Safety
Memory safety in AI agents is defined at the boundary of retrieval: only a per-retrieval, provenance-logged audit can benchmark or enforce product-grade memory safety.
## Purpose
The Article introduces the Retrieval Boundary Audit (RBA) protocol as a stepwise, per-retrieval memory safety benchmark. A reference implementation is necessary: it directly supports the thesis by making RBA audits testable, reproducible, and inspectable by researchers and product builders. Standalone code to log, score, and export retrieval events substantiates the Article's claims.
## Generated Notes
Reference code for the RBA memory safety benchmark, as proposed in “Auditing Agent Memory: A Retrieval-Focused Benchmark for Real-World Workflow Safety.”

## What is RBA?
RBA scores agents on *per-retrieval* fidelity, boundary, provenance, and latency. Instead of evaluating only storage/recall rates, RBA audits every memory retrieval event during a workflow for:
- Provenance: Where was it recalled from?
- Boundary: Was it inside correct user/session/scope?
- Latency: How long did it take?
- Outcome: Correct, omitted, cross-boundary, or error.

## Usage
- Log agent memory retrieval events using the provided schema.
- Optionally, annotate ambiguous or adversarial traces.
- Run the scorer to audit per-step fidelity, boundary, and latency.
- Use sample traces in `examples/` as reference.

## File structure
- `rba_schema.py`: Python schema (dataclass) for retrieval events.
- `rba_logger.py`: Functions to log and append events.
- `rba_scorer.py`: Scores a retrieval trace (JSONL) with boundary/error metrics.
- `examples/example_rba_trace.jsonl`: Demo trace for an agent workflow.

## Citation
See the Article and references for background: [Auditing Agent Memory... (Aetna, 2024)](https://arxiv.org/abs/2310.08560) and linked prior art.
## Files
- `README.md`: Documents the benchmark rationale, usage, file format, and experiment workflow for RBA.
- `rba_schema.py`: Defines a dataclass (and JSON schema) for retrieval events, ensuring consistent provenance and boundary logging.
- `rba_logger.py`: Utility to log/append retrieval events as JSON Lines for later scoring or review.
- `rba_scorer.py`: Scores a retrieval trace (JSONL) using RBA's protocol: per-retrieval fidelity, boundary adherence, latency, and error count.
- `examples/example_rba_trace.jsonl`: Sample RBA trace file for a hypothetical agent workflow. Useful for demonstration and scoring.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Documents the benchmark rationale, usage, file format, and experiment workflow for RBA.
- `rba_schema.py`: Defines a dataclass (and JSON schema) for retrieval events, ensuring consistent provenance and boundary logging.
- `rba_logger.py`: Utility to log/append retrieval events as JSON Lines for later scoring or review.
- `rba_scorer.py`: Scores a retrieval trace (JSONL) using RBA's protocol: per-retrieval fidelity, boundary adherence, latency, and error count.
- `examples/example_rba_trace.jsonl`: Sample RBA trace file for a hypothetical agent workflow. Useful for demonstration and scoring.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.