# aetna-research-lab
Minimal reference implementation of the Retrieval Boundary Audit (RBA) protocol for benchmarking agent memory boundary fidelity.
## Article
When Agent Memory Fails: Benchmarking Retrieval Boundary Breaches, Not Just Recall
The defining benchmark for agent memory safety is live, provenance-tagged retrieval boundary auditing, not storage size or overall recall.
## Purpose
The article proposes a Retrieval Boundary Audit (RBA) protocol that benefits from a minimal reference implementation demonstrating per-retrieval logging and boundary scoring. This repo provides a prototype scoring harness that makes the benchmark concrete.
## Generated Notes
Minimal reference implementation of the Retrieval Boundary Audit (RBA) protocol for benchmarking agent memory boundary fidelity.
## Article
When Agent Memory Fails: Benchmarking Retrieval Boundary Breaches, Not Just Recall
The defining benchmark for agent memory safety is live, provenance-tagged retrieval boundary auditing, not storage size or overall recall.
## Purpose
The article proposes a Retrieval Boundary Audit (RBA) protocol that benefits from a minimal reference implementation demonstrating per-retrieval logging and boundary scoring. This repo provides a prototype scoring harness that makes the benchmark concrete.
## Generated Notes
... (full content as above, but I'll keep it in the JSON as a string)
## Files
- `README.md`: Project overview, quickstart, and usage notes
- `rba_protocol.py`: Core protocol implementation: event scoring, trace processing, and example runner
- `example_trace.json`: Sample retrieval trace with boundary hits, misses, cross events, and errors
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Project overview, quickstart, and usage notes
- `rba_protocol.py`: Core protocol implementation: event scoring, trace processing, and example runner
- `example_trace.json`: Sample retrieval trace with boundary hits, misses, cross events, and errors
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.