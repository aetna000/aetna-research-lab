# aetna-research-lab
Reference benchmark for stepwise evidence-chain logging and scoring in synthetic UI product agent workflows.
## Article
The Smallest Benchmark That Breaks Agent Trust: Stepwise Evidence Chains in Real UIs
Product-ready multimodal agents are only trustworthy if they expose replayable, auditable evidence chains for every UI step, not just generated actions.
## Purpose
The Article's central proposal is a minimal, auditable benchmark for agent evidence chains across synthetic UI screens. Credibility, reproducibility, and uptake improve if a reference implementation for the benchmark harness, evidence chain data structures, and sample evaluation pipeline are public. Without code, the proposal risks remaining just another conceptual framework.
## Generated Notes
Reference benchmark for stepwise evidence-chain logging and scoring in synthetic UI product agent workflows.
## Article
The Smallest Benchmark That Breaks Agent Trust: Stepwise Evidence Chains in Real UIs
Product-ready multimodal agents are only trustworthy if they expose replayable, auditable evidence chains for every UI step, not just generated actions.
## Purpose
The Article's central proposal is a minimal, auditable benchmark for agent evidence chains across synthetic UI screens. Credibility, reproducibility, and uptake improve if a reference implementation for the benchmark harness, evidence chain data structures, and sample evaluation pipeline are public. Without code, the proposal risks remaining just another conceptual framework.
## Generated Notes
Minimal benchmark harness and data schema to test if product AI agents can log and expose full evidence chains, screen state, intent, action, and outcome, across synthetic UI workflows.

## What is this?
Benchmarks whether an agent can produce a stepwise, auditable trace for each UI view: what it saw, what it inferred (intent), what it did (action), and what changed (outcome). Auditors can replay the workflow and score each evidence link.

*Motivation: Most agents can act, but not expose replayable evidence. This repo enables empirical, auditable trust testing.*

## Key files
- `schemas.py`: Data models for UI state, agent evidence chain, and workflow logs.
- `synthetic_ui.py`: Example synthetic UI task sequence (ambiguous/multi-step).
- `evaluate.py`: Harness to simulate agent runs, collect logs, and score evidence-chain completeness.
- `examples/`: Sample fixtures and outputs.

## Minimal Usage Example
1. Define or modify a UI screen sequence in `synthetic_ui.py`.
2. Simulate agent evidence chain via `evaluate.py` (or plug in your agent).
3. Run audit scoring for step completeness, breakdown visualization, or further analysis.

## Why not more?
This is a research starter kit: designed for clarity, auditability, and extension, not for production or SOTA model evaluation.

## References
See "The Smallest Benchmark That Breaks Agent Trust: Stepwise Evidence Chains in Real UIs" (Aetna, 2026).
## Files
- `README.md`: Orient researchers and product engineers to the purpose, scope, and minimal usage of the evidence-chain benchmark.
- `schemas.py`: Python dataclasses for evidence-chain benchmarking: defines Screen, Intent, Action, Outcome, and EvidenceChain trace structure.
- `synthetic_ui.py`: Defines an example sequence of synthetic UI screens and expected state transitions, source for agent benchmarking.
- `evaluate.py`: Minimal harness to simulate an agent evidence-chain run, score presence of screen, intent, action, outcome at each step, and print breakdown.
- `examples/evidence_chain_sample.json`: Fixture: synthetic evidence chain for auditing, demonstration, or test input.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Orient researchers and product engineers to the purpose, scope, and minimal usage of the evidence-chain benchmark.
- `schemas.py`: Python dataclasses for evidence-chain benchmarking: defines Screen, Intent, Action, Outcome, and EvidenceChain trace structure.
- `synthetic_ui.py`: Defines an example sequence of synthetic UI screens and expected state transitions, source for agent benchmarking.
- `evaluate.py`: Minimal harness to simulate an agent evidence-chain run, score presence of screen, intent, action, outcome at each step, and print breakdown.
- `examples/evidence_chain_sample.json`: Fixture: synthetic evidence chain for auditing, demonstration, or test input.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.