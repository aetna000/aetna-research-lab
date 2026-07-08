# aetna-research-lab
Reference implementation of the Local LLM Action Audit Card protocol for stepwise action verification in local LLM agents.
## Article
Action Audit Trails for Local LLMs: Proving What Changed, Not Just What Clicked
The missing layer for trustworthy local LLM agents is a practical, per-step action audit card that logs not just the action, but the input evidence, memory, permission, and workflow delta, making every change replayable and product-grade auditable.
## Purpose
The article proposes a concrete audit protocol but no implementation. Providing a minimal reference implementation in Python demonstrates the protocol's feasibility and serves as a starting point for integration into local LLM agent stacks, directly supporting the article's credibility.
## Generated Notes
Reference implementation of the Local LLM Action Audit Card protocol for stepwise action verification in local LLM agents.
## Article
Action Audit Trails for Local LLMs: Proving What Changed, Not Just What Clicked
The missing layer for trustworthy local LLM agents is a practical, per-step action audit card that logs not just the action, but the input evidence, memory, permission, and workflow delta, making every change replayable and product-grade auditable.
## Purpose
The article proposes a concrete audit protocol but no implementation. Providing a minimal reference implementation in Python demonstrates the protocol's feasibility and serves as a starting point for integration into local LLM agent stacks, directly supporting the article's credibility.
## Generated Notes
Reference implementation of the [Local LLM Action Audit Card](https://x.com/aetna000) protocol described in _Action Audit Trails for Local LLMs: Proving What Changed, Not Just What Clicked_.

## What is the audit card?

For every agent step on a local inference engine, we record:

1. **Input evidence** (screen, UI, or state snapshot)
2. **Memory/context** fed to the model
3. **Workflow permission** state
4. **Proposed action** with risk classification
5. **Delta** in workflow/state after the action
6. **Verification** that the intended change occurred

This makes every step auditable, essential for product-grade trust.

## Repository structure

- `audit_card.py`, Core protocol definition and `AuditCard` class
- `example_usage.py`, Manual example with mock data

## Usage

```python
from audit_card import AuditCard

# Start a new audit card for a step
card = AuditCard(
    step_id=1, input_evidence="screenshot_001.png", memory_context="User requested file rename", permission="user", proposed_action="rename file.txt to report.txt", risk="low"
)

# Simulate action execution and record delta
card.record_delta(before={"files": ["file.txt"]}, after={"files": ["report.txt"]})
card.verify_outcome(success=True, notes="File renamed as intended")

# Get full record
print(card.to_dict())
```

See `example_usage.py` for more details.

## Integration with local LLM stacks

This protocol can be embedded into agents built with llama.cpp, Ollama, vLLM, or other local inference libraries. The audit card is hardware-agnostic and requires only the ability to log state snapshots and deltas.

## Contributing

Feedback, extensions, and integrations are welcome. Please open an issue or pull request.

## Citation

```bibtex
@misc{aetna2025auditcards, title={{Action Audit Trails for Local LLMs: Proving What Changed, Not Just What Clicked}}, author={Aetna}, year={2025}, howpublished={\url{https://x.com/aetna000}}, }
```
## Files
- `README.md`: Explain the protocol, the code, usage, and relationship to the research article.
- `audit_card.py`: Provides the AuditCard class implementing the Local LLM Action Audit Card protocol.
- `example_usage.py`: Demonstrate manual creation of audit steps with mock data to illustrate the protocol.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Explain the protocol, the code, usage, and relationship to the research article.
- `audit_card.py`: Provides the AuditCard class implementing the Local LLM Action Audit Card protocol.
- `example_usage.py`: Demonstrate manual creation of audit steps with mock data to illustrate the protocol.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.