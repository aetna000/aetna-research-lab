# aetna-research-lab
Minimal benchmark harness for stepwise Screen-Intent-Action-Outcome (SIAO) evidence chains in UI agent workflows.
## Article
The Real Test for Multimodal Agents: Stepwise Evidence, Not Just Actions
The product bottleneck for multimodal AI agents is not action generation; it is exposing evidence that links screen, intent, action, and outcome.
## Purpose
The Article's main thesis is a concrete stepwise evidence-chain benchmark for multimodal agents. The public repo must provide a minimal but runnable evaluation harness (schema, logging template, scoring, and example workflow) to make the claim actionable and differentiable from pure theory.
## Generated Notes
Minimal benchmark harness for stepwise Screen-Intent-Action-Outcome (SIAO) evidence chains in UI agent workflows.
## Article
The Real Test for Multimodal Agents: Stepwise Evidence, Not Just Actions
The product bottleneck for multimodal AI agents is not action generation; it is exposing evidence that links screen, intent, action, and outcome.
## Purpose
The Article's main thesis is a concrete stepwise evidence-chain benchmark for multimodal agents. The public repo must provide a minimal but runnable evaluation harness (schema, logging template, scoring, and example workflow) to make the claim actionable and differentiable from pure theory.
## Generated Notes
Minimal, open benchmark harness for evaluating stepwise Screen-Intent-Action-Outcome (SIAO) evidence traces in multimodal UI agents.

## Why?
Most agent stacks log actions or outputs, but not the evidence chain from screen state, inferred intent, action choice, to outcome. Auditable and trustworthy agents must expose this full trace for every step in the workflow ([see Article](https://arxiv.org/abs/2210.03347)).

## What does this repo provide?
- A lightweight evaluation harness for collecting SIAO traces with synthetic or real UI screens.
- Log/data schema and sample logger for SIAO stepwise evidence.
- Score script: checks chain completeness, attribution, and type of breakdowns.
- Example: a synthetic UI workflow with example agent outputs and audit labels.

## Usage
- Run `python example_run.py` to simulate a workflow and log agent SIAO steps.
- Inspect `out/evidence_chain_example.jsonl` for artifact format.
- Use `score_benchmark.py` to tally missing links or attribution errors.

For research or audit community input. No proprietary agent code.
## Files
- `README.md`: Gives benchmark motivation, protocol, design, and usage steps so researchers can reproduce the evidence-chain evaluation.
- `siao_schema.py`: Defines the minimal Python schema and I/O for capturing and validating stepwise SIAO evidence-chain logs.
- `example_run.py`: Demonstrates a toy workflow: 2-step simulated UI, example agent SIAO trace, and output artifact for scoring.
- `score_benchmark.py`: Implements SIAO benchmark scoring: checks for trace completeness and labels failure classes.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Gives benchmark motivation, protocol, design, and usage steps so researchers can reproduce the evidence-chain evaluation.
- `siao_schema.py`: Defines the minimal Python schema and I/O for capturing and validating stepwise SIAO evidence-chain logs.
- `example_run.py`: Demonstrates a toy workflow: 2-step simulated UI, example agent SIAO trace, and output artifact for scoring.
- `score_benchmark.py`: Implements SIAO benchmark scoring: checks for trace completeness and labels failure classes.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.