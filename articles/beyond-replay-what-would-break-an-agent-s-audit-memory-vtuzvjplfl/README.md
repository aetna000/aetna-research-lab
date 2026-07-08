# aetna-research-lab
Reference code for adversarial memory boundary auditing in multimodal product AI agents, as proposed in the MBAH X Article.
## Article
Beyond Replay: What Would Break an Agent’s Audit, Memory Isolation or Persistent State Leaks?
Trustworthy multimodal agents for product workflows must expose not just their memory, but explicit boundaries, what is remembered, forgotten, or isolated across steps, so products can prove auditability and prevent silent, persistent failures.
## Purpose
The article proposes a stepwise, adversarial memory boundary audit harness (MBAH) for multimodal agents, which is what makes the research novel and actionable for product teams. A minimal reference implementation providing a runnable harness for memory auditing (with agent interface and adversarial tests) is essential to support the thesis, make benchmarking reproducible, and help teams adopt or extend the method.
## Generated Notes
Reference code for adversarial memory boundary auditing in multimodal product AI agents, as proposed in the MBAH X Article.
## Article
Beyond Replay: What Would Break an Agent’s Audit, Memory Isolation or Persistent State Leaks?
Trustworthy multimodal agents for product workflows must expose not just their memory, but explicit boundaries, what is remembered, forgotten, or isolated across steps, so products can prove auditability and prevent silent, persistent failures.
## Purpose
The article proposes a stepwise, adversarial memory boundary audit harness (MBAH) for multimodal agents, which is what makes the research novel and actionable for product teams. A minimal reference implementation providing a runnable harness for memory auditing (with agent interface and adversarial tests) is essential to support the thesis, make benchmarking reproducible, and help teams adopt or extend the method.
## Generated Notes
Reference implementation for the adversarial memory audit benchmark described in the Article "Beyond Replay: What Would Break an Agent’s Audit, Memory Isolation or Persistent State Leaks?"

## Purpose
Audits a multimodal agent's memory at every workflow step, simulating adversarial state changes (e.g., user/session switch, permission downgrade) and verifying whether retained state, forgotten context, and boundary failures are made explicit.

## Features
- Stepwise agent, harness checkpointing and audit
- Adversarial context injections (switches, wipes, permission changes)
- Minimal agent interface, adaptable to real or synthetic agents
- Replayable audit trace for every workflow step

## Example Usage
```bash
python harness.py fixtures/ui_workflow_example.json
```

## Files
- harness.py, main audit harness
- agent_stub.py, minimal agent interface for demonstration
- fixtures/ui_workflow_example.json, sample workflow with adversarial transitions

## License
MIT (for research use; no production guarantees)
## Files
- `README.md`: Documents the goals, setup, and usage of the harness for researchers and builders.
- `harness.py`: Core implementation of the memory boundary audit harness, orchestrating workflow steps, agent probes, adversarial transitions, and audit scoring.
- `agent_stub.py`: Minimal agent stub providing observable memory behavior, to demonstrate harness protocol and adversarial perturbations.
- `fixtures/ui_workflow_example.json`: Provides a synthetic UI workflow with stepwise context and adversarial transitions to demo the audit.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Documents the goals, setup, and usage of the harness for researchers and builders.
- `harness.py`: Core implementation of the memory boundary audit harness, orchestrating workflow steps, agent probes, adversarial transitions, and audit scoring.
- `agent_stub.py`: Minimal agent stub providing observable memory behavior, to demonstrate harness protocol and adversarial perturbations.
- `fixtures/ui_workflow_example.json`: Provides a synthetic UI workflow with stepwise context and adversarial transitions to demo the audit.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.