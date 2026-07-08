# aetna-research-lab
Reference Python for the agent boundary audit card: scoring, schema, and example for workflow benchmark step tracing.
## Article
A Small Benchmark for Agent Boundary Failures After MemGPT: Towards LLMs as Operating S...
The product bottleneck for workflow benchmarks and evaluation design is not only model capability; it is whether each boundary in the agent step can be audited.
## Purpose
The Article claims a minimal audit-card protocol as a new benchmark primitive. A reference code artifact providing a readable, runnable implementation (audit card schema, scoring, and example trace) is necessary for credibility, reproducibility, and inviting readers to inspect/adapt the approach for their own agents or workflow evaluations.
## Generated Notes
Reference Python for the agent boundary audit card: scoring, schema, and example for workflow benchmark step tracing.
## Article
A Small Benchmark for Agent Boundary Failures After MemGPT: Towards LLMs as Operating S...
The product bottleneck for workflow benchmarks and evaluation design is not only model capability; it is whether each boundary in the agent step can be audited.
## Purpose
The Article claims a minimal audit-card protocol as a new benchmark primitive. A reference code artifact providing a readable, runnable implementation (audit card schema, scoring, and example trace) is necessary for credibility, reproducibility, and inviting readers to inspect/adapt the approach for their own agents or workflow evaluations.
## Generated Notes
Reference Python for the minimal audit card protocol from "A Small Benchmark for Agent Boundary Failures After MemGPT".

## What is this?
A research prototype for logging, scoring, and inspecting boundary evidence in agent workflow steps:
- Observation, inference, memory/state, permission, action, outcome
- For each step: record what the agent relied on, assess failure types, report per-boundary audit, not just task success

## How to use
- See `audit_card.py` for the schema, scoring logic, and example usage.
- Run `python audit_card.py` to simulate three agent steps with ambiguous boundaries and print the audit output.

## Example output
```
--- Audit Card 1 ---
Claim: User intends to approve transfer
Evidence: {'type': 'ui_observation', 'content': 'Approve Transfer button is highlighted'}
Memory/State: {'last_action': 'entered amount', 'session_timeout': False}
Permission: {'required': 'can_initiate_transfer', 'actual': 'user'}
Action: initiate_transfer
Expected Outcome: Transfer approved
Post-state: {'transfer_status': 'pending'}
Failures: ['ambiguous_intent']

--- Audit Card 2 ---
Claim: Amount is within policy
Evidence: {'type': 'memory', 'content': 'max allowed = 5000'}
Memory/State: {'amount': 7000}
Permission: {'required': 'manager', 'actual': 'user'}
Action: proceed_transfer
Expected Outcome: Transfer processed
Post-state: {'error': 'Permission denied'}
Failures: ['permission_gap']
...
```

## Limitations
- This is a research scaffold only. No persistent storage, security, or real integration. 
- Scoring is heuristic and domain-agnostic.
## Files
- `README.md`: Explain the audit card concept, how to use the code, limitations, and show an example output.
- `audit_card.py`: Contains the minimal boundary audit card schema, scoring logic, and three example workflow traces.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Explain the audit card concept, how to use the code, limitations, and show an example output.
- `audit_card.py`: Contains the minimal boundary audit card schema, scoring logic, and three example workflow traces.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.