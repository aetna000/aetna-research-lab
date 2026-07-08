# aetna-research-lab
Reference harness and schema for benchmarking AI agent memory safety with stepwise Retrieval Boundary Audit (RBA) logs, boundary scoring, and provenance.
## Article
When Agent Memory Breaks: A Benchmark for Retrieval-Boundary Breaches, Not Recall Size
Agent memory safety is best measured by stepwise audits of live retrievals, provenance-tagged, boundary-tested, and latency-logged, not by aggregate recall or storage claims.
## Purpose
The Article proposes a new benchmark protocol, Retrieval Boundary Audit (RBA), to measure agent memory safety in real workflows, explicitly defining per-retrieval logging, provenance, boundary scoring, and latency capture. Sharing a minimal but actionable reference implementation (logging harness, scoring logic, dataset schema) is necessary to demonstrate feasibility, enable replication, and support future comparisons/leaderboards for trustworthy agent memory.
## Generated Notes
Reference harness and schema for benchmarking AI agent memory safety with stepwise Retrieval Boundary Audit (RBA) logs, boundary scoring, and provenance.
## Article
When Agent Memory Breaks: A Benchmark for Retrieval-Boundary Breaches, Not Recall Size
Agent memory safety is best measured by stepwise audits of live retrievals, provenance-tagged, boundary-tested, and latency-logged, not by aggregate recall or storage claims.
## Purpose
The Article proposes a new benchmark protocol, Retrieval Boundary Audit (RBA), to measure agent memory safety in real workflows, explicitly defining per-retrieval logging, provenance, boundary scoring, and latency capture. Sharing a minimal but actionable reference implementation (logging harness, scoring logic, dataset schema) is necessary to demonstrate feasibility, enable replication, and support future comparisons/leaderboards for trustworthy agent memory.
## Generated Notes
## Overview
This research prototype provides minimal logging, annotation, and scoring tools for Retrieval Boundary Audit, a protocol to measure memory safety in AI agent workflows. Each memory retrieval is logged with retrieval query, intended scope, provenance, outcome label, and latency.

- **artifact use:** Prototype for studies cited in "When Agent Memory Breaks..." (Aetna, 2024)
- **benchmarks:** Not a real agent, but a research scaffold for dataset creation, audit, and metric design

## Files
- `rba_logger.py`: API to log retrieval events in product or simulated workflows 
- `rba_dataset_schema.json`: Dataset schema for annotated retrieval logs
- `rba_score.py`: Simple scoring to report boundary/latency statistics from RBA logs
- `examples/example_trace.jsonl`: Sample annotated event trace (for illustration)

## Install & Run
No dependencies beyond Python 3.8+ standard library.

```bash
python rba_score.py --input examples/example_trace.jsonl
```

## Example: Log a retrieval event
```python
from rba_logger import RBAEvent, RBAEventLogger
logger = RBAEventLogger('my_rba_trace.jsonl')
event = RBAEvent(
    query="fetch user X's doc A", intent_scope={"user": "X", "session": "S1"}, provenance={"source": "doc:A", "ui_hash": "abc"}, latency_ms=45, workflow={'step_id': '12', 'timestamp_iso': '2024-06-20T15:32:00Z'}, outcome='CROSS-BOUNDARY', notes='Crossed user boundary'
)
logger.log(event)
```

## Citation
See Article: "When Agent Memory Breaks: A Benchmark for Retrieval-Boundary Breaches, Not Recall Size" (Aetna, 2024)
## Files
- `README.md`: Repository overview, installation, and usage for researchers to audit agent memory with the RBA protocol.
- `rba_logger.py`: Core logging library: defines event dataclass, logger, and event serialization to JSONL.
- `rba_dataset_schema.json`: Defines the record schema for RBA logs for sharing/annotation/baseline scoring.
- `rba_score.py`: Script to load a .jsonl of RBA events and print summary stats by outcome, latency, and boundary error rate.
- `examples/example_trace.jsonl`: Fixture example: small annotated trace for testing RBA scoring and sharing format.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Repository overview, installation, and usage for researchers to audit agent memory with the RBA protocol.
- `rba_logger.py`: Core logging library: defines event dataclass, logger, and event serialization to JSONL.
- `rba_dataset_schema.json`: Defines the record schema for RBA logs for sharing/annotation/baseline scoring.
- `rba_score.py`: Script to load a .jsonl of RBA events and print summary stats by outcome, latency, and boundary error rate.
- `examples/example_trace.jsonl`: Fixture example: small annotated trace for testing RBA scoring and sharing format.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.