# aetna-research-lab
Reference LRPA (Live Retrieval Policy Audit) harness and log schema for benchmarking retrieval safety in AI agent memory.
## Article
What Makes AI Agent Memory Safe? Advancing Beyond Storage with Live Retrieval Policy Audits
Memory safety in AI agents is defined not by storage or logging completeness, but by verifiable enforcement of retrieval boundaries, measured as the agent’s ability to block, report, or time out on boundary-violating lookups in live workflow contexts.
## Purpose
The Article proposes a concrete protocol, Live Retrieval Policy Audit (LRPA), for benchmarking retrieval-boundary enforcement in agent memory. A minimal, reference implementation of the LRPA harness (with adversarial retrieval probes and per-step logging) makes the Article actionable, credible, and reusable by other researchers or builders. It provides a testbed for product agents, supporting both benchmarking and incident trace augmentation.
## Generated Notes
Reference LRPA (Live Retrieval Policy Audit) harness and log schema for benchmarking retrieval safety in AI agent memory.
## Article
What Makes AI Agent Memory Safe? Advancing Beyond Storage with Live Retrieval Policy Audits
Memory safety in AI agents is defined not by storage or logging completeness, but by verifiable enforcement of retrieval boundaries, measured as the agent’s ability to block, report, or time out on boundary-violating lookups in live workflow contexts.
## Purpose
The Article proposes a concrete protocol, Live Retrieval Policy Audit (LRPA), for benchmarking retrieval-boundary enforcement in agent memory. A minimal, reference implementation of the LRPA harness (with adversarial retrieval probes and per-step logging) makes the Article actionable, credible, and reusable by other researchers or builders. It provides a testbed for product agents, supporting both benchmarking and incident trace augmentation.
## Generated Notes
Reference implementation for the Live Retrieval Policy Audit (LRPA) protocol, as introduced in the article "What Makes AI Agent Memory Safe? Advancing Beyond Storage with Live Retrieval Policy Audits".

## Purpose

Benchmark AI agent memory retrieval safety by instrumenting agents to log every retrieval decision, including successful accesses, policy-blocked queries, and ambiguous attempts. Enable reproducible, adversarial evaluation of retrieval boundaries.

## Features
- Simulate in-session, cross-session, and ambiguous retrieval queries.
- Log all retrieval attempts with outcome (allow/block), provenance, policy context, rationale, and latency.
- Output audit-ready JSON logs for downstream analysis.

## Quick Start

```bash
python lrpa_harness.py --scenario fixtures/minimal_scenario.json
```

Examine the resulting log:
```
cat logs/lrpa_audit_log.json
```

## Files
- `lrpa_harness.py`: Command-line evaluation driver for LRPA scenarios.
- `lrpa_schema.py`: Log/event schema and policy-check logic.
- `fixtures/minimal_scenario.json`: Example workflow with mixed retrieval probes.
- `logs/lrpa_audit_log.json`: Output log with retrieval steps, verdicts, rationale, and timing.

## Article Reference
Implements and demonstrates the LRPA protocol as described in the Article (citation below).

## Citation
See: "What Makes AI Agent Memory Safe? Advancing Beyond Storage with Live Retrieval Policy Audits"
## Files
- `README.md`: Explains the LRPA protocol, provides usage and context for the harness, and connects code to Article claims.
- `lrpa_schema.py`: Defines log schema, decision rationale fields, and policy enforcement logic for LRPA events.
- `lrpa_harness.py`: Runs a sample workflow scenario (from a fixture), applies policy checks, logs each retrieval action, and writes audit logs.
- `fixtures/minimal_scenario.json`: Provides a minimal evaluation scenario with retrieval probes: in-session, cross-session, ambiguous, and distractor.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Explains the LRPA protocol, provides usage and context for the harness, and connects code to Article claims.
- `lrpa_schema.py`: Defines log schema, decision rationale fields, and policy enforcement logic for LRPA events.
- `lrpa_harness.py`: Runs a sample workflow scenario (from a fixture), applies policy checks, logs each retrieval action, and writes audit logs.
- `fixtures/minimal_scenario.json`: Provides a minimal evaluation scenario with retrieval probes: in-session, cross-session, ambiguous, and distractor.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.