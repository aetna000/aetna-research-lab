# aetna-research-lab
Reference code for benchmarking Retrieval Boundary Differential (RBD), auditing what agents omit, forget, or redact at workflow boundaries.
## Article
The Retrieval Boundary Problem: Benchmarking What Agents Shouldn’t Remember, Not Just What They Recall
Benchmarking memory safety in agents requires operationally defining, auditing, and testing retrieval boundaries, including what is deliberately excluded or forgotten, not merely logging what is accessed or recalled.
## Purpose
The Article introduces the Retrieval Boundary Differential (RBD) benchmark as an operational protocol to audit agent retrieval boundaries. A reference implementation (schema + basic agent harness) is necessary to demonstrate concrete application, support reproducibility, and help readers audit or extend the methodology. This code makes the Article credible and actionable.
## Generated Notes
Reference code for benchmarking Retrieval Boundary Differential (RBD), auditing what agents omit, forget, or redact at workflow boundaries.
## Article
The Retrieval Boundary Problem: Benchmarking What Agents Shouldn’t Remember, Not Just What They Recall
Benchmarking memory safety in agents requires operationally defining, auditing, and testing retrieval boundaries, including what is deliberately excluded or forgotten, not merely logging what is accessed or recalled.
## Purpose
The Article introduces the Retrieval Boundary Differential (RBD) benchmark as an operational protocol to audit agent retrieval boundaries. A reference implementation (schema + basic agent harness) is necessary to demonstrate concrete application, support reproducibility, and help readers audit or extend the methodology. This code makes the Article credible and actionable.
## Generated Notes
Reference implementation supporting the X Article:
*The Retrieval Boundary Problem: Benchmarking What Agents Shouldn’t Remember, Not Just What They Recall*

## What is this?
RBD tests operational memory safety for AI agents, by logging not just what an agent retrieves, but what it _didn't_ retrieve (with reasons), at every workflow step. This helps researchers and product teams audit privacy boundaries, permission drifts, and real evidence isolation.

## Code Contents
- [`rbd_schema.py`](rbd_schema.py): Type definitions for RBD step logs and workflow structure.
- [`rbd_agent_harness.py`](rbd_agent_harness.py): Example agent wrapper for logging both retrievals and explicit omissions.
- [`example_trace.json`](example_trace.json): Simulated workflow trace showing full RBD logging (retrieved, omitted, boundary events, stepwise justification).

## Quickstart
```bash
python rbd_agent_harness.py
```

## Example Output
See [`example_trace.json`](example_trace.json) for a boundary event where an agent must _not_ retrieve prior user memory after a session switch.

## Why?
Standard recall logs audit what agents see; RBD exposes what agents actively _forget_, _omit_, or _redact_, at the boundaries that matter for privacy and product safety.

Citation: Retrieval Boundary Differential (RBD) Benchmark: Operational Memory Safety in Agents.
## Files
- `README.md`: Entry-point: explains RBD benchmark rationale, usage, and files with example for agent stack architects.
- `rbd_schema.py`: Defines Python dataclasses for RBD benchmark: retrievals, omissions, reasons, and workflow boundaries.
- `rbd_agent_harness.py`: Simulates an agent with RBD step logging: retrieves, omits, and logs memory with omission policy.
- `example_trace.json`: Sample output of RBD agent harness: workflow with a boundary transition, showing retrievals and explicit omissions.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Entry-point: explains RBD benchmark rationale, usage, and files with example for agent stack architects.
- `rbd_schema.py`: Defines Python dataclasses for RBD benchmark: retrievals, omissions, reasons, and workflow boundaries.
- `rbd_agent_harness.py`: Simulates an agent with RBD step logging: retrieves, omits, and logs memory with omission policy.
- `example_trace.json`: Sample output of RBD agent harness: workflow with a boundary transition, showing retrievals and explicit omissions.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.