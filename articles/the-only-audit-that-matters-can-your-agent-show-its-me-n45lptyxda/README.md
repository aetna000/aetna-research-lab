# aetna-research-lab
Minimal benchmark: stepwise evidence-chain logs for screen, intent, action, and outcome in synthetic UI agent workflows.
## Article
The Only Audit That Matters: Can Your Agent Show Its Memory and Evidence Chain, Step by Step?
The central bottleneck for trustworthy product-grade multimodal agents is not action generation, but the lack of operational, replayable evidence-chain logging that ties screen, intent, action, and outcome at each workflow step.
## Purpose
The credibility and utility of the proposed SIAO Replay Benchmark depend on having a minimal, inspectable benchmark harness that lets builders or researchers simulate stepwise evidence-chain logs for UI agent workflows. A clean reference provides clarity, invites peer challenge, and addresses founder skepticism over the article's operational proposals.
## Generated Notes
Minimal benchmark: stepwise evidence-chain logs for screen, intent, action, and outcome in synthetic UI agent workflows.
## Article
The Only Audit That Matters: Can Your Agent Show Its Memory and Evidence Chain, Step by Step?
The central bottleneck for trustworthy product-grade multimodal agents is not action generation, but the lack of operational, replayable evidence-chain logging that ties screen, intent, action, and outcome at each workflow step.
## Purpose
The credibility and utility of the proposed SIAO Replay Benchmark depend on having a minimal, inspectable benchmark harness that lets builders or researchers simulate stepwise evidence-chain logs for UI agent workflows. A clean reference provides clarity, invites peer challenge, and addresses founder skepticism over the article's operational proposals.
## Generated Notes
Minimal Python reference for the Screen, Intent, Action, Outcome (SIAO) Replay Benchmark for trustworthy multimodal AI agents in UI workflows.

**Purpose:**
- Simulate stepwise evidence-chain logging across screen, intent, action, and outcome for synthetic UI tasks.
- Expose/replay full decision trace for each workflow episode.
- Score auditability (not just task success), can an auditor replay and attribute reasoning at every step?

**NOT included:** No agent models, no UI automation, no real data, no claims of product reliability. This is a research scaffold only.

## Quick Start

1. Clone this repo.
2. Run `python main.py` to simulate example SIAO-trace episodes.
3. Inspect output logs in `outputs/` or print to console.

## Structure
- `siao.py`: Core data/logic for SIAO traces (screen, intent, action, outcome, memory).
- `tasks.py`: Example synthetic UI tasks (ambiguous/multi-step screens).
- `main.py`: Runs the benchmark loop, saves trace logs for review.
- `audit_scoring.py`: Example auditor checks (Was evidence/intent surfaced? Is replay possible?).


## Example Episode Output

Screen: {'elements': [{'id': 'submit', 'text': 'Submit'}, ...]}
Intent: {'type': 'submit_form', 'cited_elements': ['submit']}
Action: {'type': 'click', 'element_id': 'submit'}
Outcome: {'ui_change': 'form_submitted'}
Memory: {...}

## Citation
See main Article: "The Only Audit That Matters: Can Your Agent Show Its Memory and Evidence Chain, Step by Step?" (@aetna000)
## Files
- `README.md`: Intro, setup, and quick-start instructions for the benchmark harness. States clear scope: simulation only, demo tasks, no product integration.
- `siao.py`: Core dataclasses and functions for representing and logging screen state, intent, action, outcome, and agent memory at each workflow step.
- `tasks.py`: Synthetic UI workflow tasks/scenarios for agents to run through. Defines deliberately ambiguous or multi-step screens for the replay benchmark.
- `main.py`: Entry point: Loads tasks, simulates agent stepwise SIAO traces, saves or prints logs for replay/audit review.
- `audit_scoring.py`: Prototype auditor: functions to check whether each step's trace surfaces correct evidence, intent attribution, replay fidelity.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Intro, setup, and quick-start instructions for the benchmark harness. States clear scope: simulation only, demo tasks, no product integration.
- `siao.py`: Core dataclasses and functions for representing and logging screen state, intent, action, outcome, and agent memory at each workflow step.
- `tasks.py`: Synthetic UI workflow tasks/scenarios for agents to run through. Defines deliberately ambiguous or multi-step screens for the replay benchmark.
- `main.py`: Entry point: Loads tasks, simulates agent stepwise SIAO traces, saves or prints logs for replay/audit review.
- `audit_scoring.py`: Prototype auditor: functions to check whether each step's trace surfaces correct evidence, intent attribution, replay fidelity.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.