# aetna-research-lab
Reference audit-card and scoring prototype for workflow agent boundary evaluation and memory safety benchmarking.
## Article
A Small Benchmark for Agent Boundary Failures After MemGPT: Towards LLMs as Operating S...
The product bottleneck for workflow benchmarks and evaluation design is not only model capability; it is whether each boundary in the agent step can be audited.
## Purpose
A central claim of the article is the need for a concrete, replayable audit object and scoring protocol for agent workflow benchmarks and evaluation design. A minimal, inspectable Python implementation for the proposed audit card (schema, scorer, and example) makes the research claim verifiable and actionable, a step up from pure theory.
## Generated Notes
Reference audit-card and scoring prototype for workflow agent boundary evaluation and memory safety benchmarking.
## Article
A Small Benchmark for Agent Boundary Failures After MemGPT: Towards LLMs as Operating S...
The product bottleneck for workflow benchmarks and evaluation design is not only model capability; it is whether each boundary in the agent step can be audited.
## Purpose
A central claim of the article is the need for a concrete, replayable audit object and scoring protocol for agent workflow benchmarks and evaluation design. A minimal, inspectable Python implementation for the proposed audit card (schema, scorer, and example) makes the research claim verifiable and actionable, a step up from pure theory.
## Generated Notes
This reference implementation turns the audit card proposal from the X Article into a minimal, inspectable harness for workflow agent step evaluation.

## What is this?
- A compact Python implementation of an audit card that records:
  - Workflow step and user-visible claim
  - Evidence used (type, pointer)
  - Evidence role (observation, inference, permission, outcome, etc.)
  - Action justified by evidence
  - Post-action state
  - Explicit permission boundary
- A scorer that flags boundary failures (missing evidence, permission gap, unverifiable outcome, over-broad memory, etc.)

## Why?
- Product trust in agents depends on clear, replayable boundary evidence.
- This code supports research into workflow benchmarks and evaluation design as described in the X Article.

## Example: Run and inspect
```python
from audit_card import AuditCard, score_audit_card

step = AuditCard(
    workflow_step="delete-email", claim="User requested deletion of email from UI selection", evidence={
        "type": "ui_observation", "source": "screenshot_20240610.png"
    }, evidence_role="observation", permission_boundary="user-email-scope", action_proposed="delete_email(email_id=12345)", expected_outcome="email deleted", post_action_state={
        "email_exists": False
    }
)

score = score_audit_card(step)
print("Boundary failure reason(s):", score['failures'])
```

See `audit_card.py` for schema, validation, and scoring logic.
## Files
- `README.md`: Explains the purpose, rationale, usage, and example for the audit card and scoring prototype.
- `audit_card.py`: Defines the AuditCard prototype class, schema, and scoring/checking functions. Central code object.
- `example_audit_run.py`: Shows how to fill and score an audit card with a practical workflow step. Minimal, serves as both demo and fixture.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Explains the purpose, rationale, usage, and example for the audit card and scoring prototype.
- `audit_card.py`: Defines the AuditCard prototype class, schema, and scoring/checking functions. Central code object.
- `example_audit_run.py`: Shows how to fill and score an audit card with a practical workflow step. Minimal, serves as both demo and fixture.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.