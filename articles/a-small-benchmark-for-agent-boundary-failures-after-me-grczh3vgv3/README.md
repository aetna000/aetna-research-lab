# aetna-research-lab
Reference implementation of the workflow benchmarks and evaluation design audit card proposed by Aetna.
## Article
A Small Benchmark for Agent Boundary Failures After MemGPT: Towards LLMs as Operating S...
The product bottleneck for workflow benchmarks and evaluation design is not only model capability; it is whether each boundary in the agent step can be audited.
## Purpose
The Article's core contribution is a typed boundary-audit card for workflow benchmarks. A minimal reference implementation of the audit card algorithm adds credibility and allows readers to inspect or adapt the scoring logic directly.
## Generated Notes
Reference implementation of the workflow benchmarks and evaluation design audit card proposed by Aetna.
## Article
A Small Benchmark for Agent Boundary Failures After MemGPT: Towards LLMs as Operating S...
The product bottleneck for workflow benchmarks and evaluation design is not only model capability; it is whether each boundary in the agent step can be audited.
## Purpose
The Article's core contribution is a typed boundary-audit card for workflow benchmarks. A minimal reference implementation of the audit card algorithm adds credibility and allows readers to inspect or adapt the scoring logic directly.
## Generated Notes
A reference implementation of the workflow benchmarks and evaluation design audit card described in the X Article *"A Small Benchmark for Agent Boundary Failures After MemGPT: Towards LLMs as Operating S..."*.

## Concept

Agent evaluations should not only report task success. They must audit each boundary in an agent step: evidence, inference, permission, memory, action, and outcome. This script receives a sequence of agent steps, scores boundary failures separately, and reports a final success only after the boundary scores are visible.

## Audit Card Fields

For each agent step, the audit card expects:
- `step_id`: unique identifier
- `claim`: the user-visible claim the agent relied on
- `evidence_type`: one of `observation`, `inference`, `preference`, `instruction`, `permission`, `outcome`
- `evidence_source`: description of the source (UI, memory, tool, etc.)
- `proposed_action`: the smallest action justified by the evidence
- `permission_boundary`: what the agent was allowed to do
- `expected_outcome`: the predicted result
- `post_action_state`: the state observed after the action

## Boundary Failure Scoring

The algorithm flags and counts failures:
- `missing_evidence`
- `stale_state`
- `ambiguous_intent`
- `permission_gap`
- `unverifiable_outcome`
- `over_broad_memory`

The final success flag is emitted only after the boundary scores are computed.

## Usage

```bash
python audit_card.py sample_steps.json
```

The input JSON file should contain a list of step objects conforming to the above structure. The script prints the boundary scores and final success flag.

## Example

```json
[
  {
    "step_id": "1", "claim": "User wants to book flight on Aug 20", "evidence_type": "inference", "evidence_source": "previous message", "proposed_action": "search for flights Aug 20", "permission_boundary": "search only", "expected_outcome": "return list of flights", "post_action_state": "list displayed"
  }, {
    "step_id": "2", "claim": "Lowest price is $250", "evidence_type": "observation", "evidence_source": "screenshot", "proposed_action": "confirm booking", "permission_boundary": "booking requires manual approval", "expected_outcome": "booking submitted", "post_action_state": "booking pending"
  }
]
```

## Status

This is a research prototype. It does not connect to any live agent or UI; it is a standalone scoring harness.
## Files
- `README.md`: Explains the audit card concept, how to use the code, and the structure of the input/output.
- `audit_card.py`: Implements the audit card algorithm: reads step logs, scores boundary failures, and reports the final success flag.
- `sample_steps.json`: Example input file with two agent steps to demonstrate the audit card scoring.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Explains the audit card concept, how to use the code, and the structure of the input/output.
- `audit_card.py`: Implements the audit card algorithm: reads step logs, scores boundary failures, and reports the final success flag.
- `sample_steps.json`: Example input file with two agent steps to demonstrate the audit card scoring.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.