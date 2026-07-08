# aetna-research-lab
Minimal benchmark harness for auditable screen-intent-action-outcome (SIAO) traces in multimodal agent workflows.
## Article
I Do Not Trust Screen Agents Without a Trace
The product bottleneck for multimodal agents is not action generation; it is evidence that makes the action trustworthy.
## Purpose
The article proposes a concrete, auditable evidence-chain evaluation procedure for agents in product workflows. A minimal, inspectable benchmark harness, including code to serialize (screen, intent, action, outcome) logs for agent steps, makes the argument credible, usable, and testable for builders.
## Generated Notes
Minimal benchmark harness for auditable screen-intent-action-outcome (SIAO) traces in multimodal agent workflows.
## Article
I Do Not Trust Screen Agents Without a Trace
The product bottleneck for multimodal agents is not action generation; it is evidence that makes the action trustworthy.
## Purpose
The article proposes a concrete, auditable evidence-chain evaluation procedure for agents in product workflows. A minimal, inspectable benchmark harness, including code to serialize (screen, intent, action, outcome) logs for agent steps, makes the argument credible, usable, and testable for builders.
## Generated Notes
Minimal research harness for logging, serializing, and replaying screen-intent-action-outcome (SIAO) traces in product workflows with multimodal agents.

## Purpose
- Provide a reference, auditable code artifact for the evaluation procedure described in the Article: I Do Not Trust Screen Agents Without a Trace.
- Let researchers and builders log agent decision steps (screen, intent, action, outcome) and analyze breakdowns by type.

## Features
- Stepwise logging of all agent decisions (each entry includes screen, parsed UI elements, inferred intent, action + rationale, and outcome state).
- Outputs replayable JSON traces for inspection, audit, or regression/debug.
- Scoring script to label/focus failures: UI grounding, intent inference, planning, attribution, or action fault.
- Pure Python, no dependencies outside the standard library (example synthetic agent & UI loop included for clarity).

## Example Run
```bash
python example_synthetic_benchmark.py
```
Will output a `siaotrace.json` file with recorded steps and a simple summary of any breakdowns.

**Note:** This is a research artifact for product agent workflow evidence-chain evaluation, not a full product or test suite.
## Files
- `README.md`: Describe the purpose, setup, and usage pattern of the evidence-chain benchmark.
- `siaobench/siaotrace.py`: Core trace logging and serialization for (screen, intent, action, outcome) decision chains.
- `siaobench/scorer.py`: Simple scoring for SIAO traces: label failures by type and print summary.
- `example_synthetic_benchmark.py`: Show a toy agent/UI loop logging SIAO chains using the benchmark artifact.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Describe the purpose, setup, and usage pattern of the evidence-chain benchmark.
- `siaobench/siaotrace.py`: Core trace logging and serialization for (screen, intent, action, outcome) decision chains.
- `siaobench/scorer.py`: Simple scoring for SIAO traces: label failures by type and print summary.
- `example_synthetic_benchmark.py`: Show a toy agent/UI loop logging SIAO chains using the benchmark artifact.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.