# aetna-research-lab
Minimal benchmark harness for agent evidence-chain logging: screen state, intent, action justification, and outcome replay.
## Article
The Real Test for Product-Grade AI Agents: Can They Expose Their Evidence, Step by Step?
The bottleneck for product-ready multimodal agents is not action generation, but full-chain evidence logging that justifies each agent step.
## Purpose
The Article proposes an auditable 'evidence-chain benchmark' for agent steps in product workflows, but such a benchmark has not been published as code. A minimal, open implementation, logging screen, intent, action, evidence, and outcome for each agent step in a UI workflow, is necessary for the Article's credibility. A reproducible harness will allow researchers and product teams to test, audit, and build on the proposal.
## Generated Notes
Minimal benchmark harness for agent evidence-chain logging: screen state, intent, action justification, and outcome replay.
## Article
The Real Test for Product-Grade AI Agents: Can They Expose Their Evidence, Step by Step?
The bottleneck for product-ready multimodal agents is not action generation, but full-chain evidence logging that justifies each agent step.
## Purpose
The Article proposes an auditable 'evidence-chain benchmark' for agent steps in product workflows, but such a benchmark has not been published as code. A minimal, open implementation, logging screen, intent, action, evidence, and outcome for each agent step in a UI workflow, is necessary for the Article's credibility. A reproducible harness will allow researchers and product teams to test, audit, and build on the proposal.
## Generated Notes
Minimal reference harness for benchmarking auditable agents in real or synthetic UI workflows. Logs every agent step:
- Pre-action screen state (image or structure)
- Detected UI elements/cues
- Inferred intent (with cited evidence)
- Chosen action (with explicit reference to screen/context)
- Action outcome (post-action state)

This supports the Article: 'The Real Test for Product-Grade AI Agents: Can They Expose Their Evidence, Step by Step?'

## What Is This?
- Reference Python harness for logging and replaying evidence chains, screen→intent→action→evidence→outcome, at every agent step.
- NOT a production agent, NOT a model, NOT tied to any SaaS or secret API.
- Provides a testable scaffold for benchmarking both synthetic and real agent decisions as artifacts.

## Quick Start
1. Clone repo.
2. See `examples/simple_scenario.json` for input structure.
3. Run `python evidence_chain.py examples/simple_scenario.json > output_chain.jsonl`.
4. Inspect chain logs for screen, intent, action, evidence, and outcome per step.

## Requirements
Python 3.7+ (standard library only)

## Files
- `evidence_chain.py`: Loads a scenario, simulates 'perception' and 'agent' steps, logs evidence chain.
- `schema.py`: Minimal data schemas for step logs.
- `examples/simple_scenario.json`: Example 2-step scenario fixture.
- `README.md`: You are here.

## Citing
If used to support agent audit or workflow research, cite as:
> Evidence-Chain Benchmark: Minimal Logging and Replay Harness (Aetna, 2024)

Reference Article: [The Real Test for Product-Grade AI Agents: Can They Expose Their Evidence, Step by Step?](https://arxiv.org/abs/2210.03347)
## Files
- `README.md`: Repository introduction, setup, usage, and links benchmark purpose to the Article.
- `evidence_chain.py`: Main harness: runs through a test scenario, logs each evidence chain step to stdout as JSON lines.
- `schema.py`: Defines the minimal evidence-chain step schema as a data class.
- `examples/simple_scenario.json`: Fixture: Example 2-step scenario with UI elements and post-action screen states.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Repository introduction, setup, usage, and links benchmark purpose to the Article.
- `evidence_chain.py`: Main harness: runs through a test scenario, logs each evidence chain step to stdout as JSON lines.
- `schema.py`: Defines the minimal evidence-chain step schema as a data class.
- `examples/simple_scenario.json`: Fixture: Example 2-step scenario with UI elements and post-action screen states.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.