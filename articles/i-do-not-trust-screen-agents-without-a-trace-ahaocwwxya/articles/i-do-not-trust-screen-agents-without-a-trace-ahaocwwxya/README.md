# Evidence-Chain Evaluation Harness

Reference implementation for the Aetna X Article “I Do Not Trust Screen Agents Without a Trace”.

## Purpose
Evaluate multimodal agent actions using linked evidence-chain artifacts: pre-action screen state, inferred user intent (with evidence), chosen action (with citation), and post-action outcome. Benchmark both task completion and auditability of evidence.

## What’s Included
- evidence_chain.py: Minimal evaluation harness.
- example_fixture.json: Example UI state and workflow input.
- chain_log_example.json: One sample stepwise evidence-chain log.

## Usage
Inspect, run, or adapt `evidence_chain.py` to:
- Accept a (simulated) pre-action screen description.
- Pass control to a placeholder agent which outputs inferred intent and a chosen action, each citing parts of the screen evidence.
- Run an outcome simulation and log the post-action screen state.
- Output a JSON chain log mapping state, intent, action, and observed result.

No external APIs, secrets, or credentials required. Pure Python. No claims of real UI/agent; this is for benchmark and idea inspection.

## Citation
If citing, use: Reference implementation for I Do Not Trust Screen Agents Without a Trace (Aetna, 2026).