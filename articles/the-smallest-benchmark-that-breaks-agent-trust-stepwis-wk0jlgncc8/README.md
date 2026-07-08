# aetna-research-lab
Minimal benchmark and schema for stepwise evidence-chain logging in UI agent workflows. Supports replay and audit as proposed by Aetna.
## Article
The Smallest Benchmark That Breaks Agent Trust: Stepwise Evidence Chains in Real UIs
Product-ready multimodal agents are only trustworthy if they expose replayable, auditable evidence chains for every UI step, not just generated actions.
## Purpose
The Article calls for a concrete, minimal evidence-chain benchmark for UI agents. A public code artifact allows agents to be evaluated stepwise for replayable auditability, exactly as demanded. Without example harness code and a schema for evidence-chain logs, the Article's benchmark claim is not actionable or credible to builders. The repo will not overclaim, just a research-grade minimal harness, schema, and synthetic example.
## Generated Notes
Minimal benchmark and schema for stepwise evidence-chain logging in UI agent workflows. Supports replay and audit as proposed by Aetna.
## Article
The Smallest Benchmark That Breaks Agent Trust: Stepwise Evidence Chains in Real UIs
Product-ready multimodal agents are only trustworthy if they expose replayable, auditable evidence chains for every UI step, not just generated actions.
## Purpose
The Article calls for a concrete, minimal evidence-chain benchmark for UI agents. A public code artifact allows agents to be evaluated stepwise for replayable auditability, exactly as demanded. Without example harness code and a schema for evidence-chain logs, the Article's benchmark claim is not actionable or credible to builders. The repo will not overclaim, just a research-grade minimal harness, schema, and synthetic example.
## Generated Notes
Minimal research benchmark and schema for stepwise, replayable evidence-chain logging in UI agent workflows, as described in [The Smallest Benchmark That Breaks Agent Trust: Stepwise Evidence Chains in Real UIs]().

## What is this?
A public prototype harness, schema, and example for evaluating UI agents on transparent evidence chains:
- At each workflow step, agent logs: screen state, inferred intent (with evidence), chosen action (+ rationale), and post-action outcome.
- All logs are chained for replay and audit.

## Who is this for?
- Researchers/engineers testing trustworthy UI agents
- Auditors and product teams evaluating AI agent claims

## Repo contents
- `evidence_chain.py`: Core class and schema for SIAO (Screen, Intent, Action, Outcome) logging and replay
- `example_synthetic.py`: Tiny simulated agent run over a 2-step toy UI, with logs
- Example JSON log output

## How do I use it?
- See `example_synthetic.py` for a synthetic 2-step run
- Review or edit `evidence_chain.py` as a hook for your real or synthetic agent stack
- Output includes detailed evidence chain logs in JSON, replayable for human or algorithmic inspection

## Citation
If you use or extend this, cite:
> aetna-evidence-chain-benchmark: Benchmark and schema for auditable, replayable UI agent evidence chains. Used in [The Smallest Benchmark That Breaks Agent Trust: Stepwise Evidence Chains in Real UIs]().
## Files
- `README.md`: Explains what the repo is, how to use the benchmark harness, and cites the Article for context.
- `evidence_chain.py`: Implements the minimal evidence-chain logging and replay schema; usable as a research harness or logging tool.
- `example_synthetic.py`: Demonstrates a toy 2-step evidence chain for a synthetic UI workflow.
- `example_evidence_chain_log.json`: Provides a sample JSON output for agent stepwise evidence logging, for quick inspection and reproducibility.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Explains what the repo is, how to use the benchmark harness, and cites the Article for context.
- `evidence_chain.py`: Implements the minimal evidence-chain logging and replay schema; usable as a research harness or logging tool.
- `example_synthetic.py`: Demonstrates a toy 2-step evidence chain for a synthetic UI workflow.
- `example_evidence_chain_log.json`: Provides a sample JSON output for agent stepwise evidence logging, for quick inspection and reproducibility.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.