# aetna-research-lab
Minimal benchmark harness for auditable stepwise evidence-chain logging in multimodal agent workflows (screen, intent, action, outcome).
## Article
No Evidence Chain, No Trust: The Stepwise Benchmark Product AI Agents Can’t Fake
Product-ready multimodal agents must expose a replayable, auditable evidence chain, screen, intent, action, outcome, for real trust.
## Purpose
The Article's credibility hinges on a concrete, inspectable protocol for stepwise, auditable agent evidence-chain logging. Readers must be able to see, run, or extend a minimal instrumented workflow to benchmark whether an agent logs screen, intent, action, and outcome for every step. No publicly available harness currently implements this standard.
## Generated Notes
Minimal benchmark harness for auditable stepwise evidence-chain logging in multimodal agent workflows (screen, intent, action, outcome).
## Article
No Evidence Chain, No Trust: The Stepwise Benchmark Product AI Agents Can’t Fake
Product-ready multimodal agents must expose a replayable, auditable evidence chain, screen, intent, action, outcome, for real trust.
## Purpose
The Article's credibility hinges on a concrete, inspectable protocol for stepwise, auditable agent evidence-chain logging. Readers must be able to see, run, or extend a minimal instrumented workflow to benchmark whether an agent logs screen, intent, action, and outcome for every step. No publicly available harness currently implements this standard.
## Generated Notes
Reference implementation of the stepwise, auditable evidence-chain protocol as proposed in "No Evidence Chain, No Trust: The Stepwise Benchmark Product AI Agents Can’t Fake" (Aetna, 2024).

This harness simulates a product workflow where, at each step, an agent must log and expose:
- The screen/UI state as observed
- Parsed UI map/focus/ambiguities
- Explicit inferred intent (with evidence references)
- The chosen action and its rationale (with supporting evidence)
- The resulting outcome/UI diff

Each workflow is replayable and auditable. Any missing or vague link in the chain counts as failure.

## Usage

```bash
python main.py
```

- See `sample_workflow.json` for input format.
- See `output_log.json` for the resulting evidence-chain trace.

## Files
- `main.py`: Runs a synthetic UI agent workflow, logging each SIAO step.
- `schema.py`: Data structures for stepwise evidence logging.
- `sample_workflow.json`: Example minimal workflow used in the harness.
- `output_log.json`: Evidence-chain output log after running the workflow.

**Citation:**
Aetna. "No Evidence Chain, No Trust: The Stepwise Benchmark Product AI Agents Can’t Fake", 2024.

For questions, issues, or contributions: open a GitHub issue or pull request.
## Files
- `README.md`: Guide users to the purpose, minimal usage, and artifact structure of the evidence-chain benchmark.
- `schema.py`: Defines data classes (Python dataclasses) for the structured, stepwise evidence-chain logs.
- `sample_workflow.json`: Provides a minimal synthetic UI workflow as input to the benchmark harness, two steps, explicit ambiguities.
- `main.py`: Runs the benchmark workflow: loads input, steps through each UI state, simulates agent 'evidence-chain' output, and writes the audit log.
- `output_log.json`: Shows an example of the evidence-chain audit log produced by running the sample workflow (for illustration, not meant to be real audit data).
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Guide users to the purpose, minimal usage, and artifact structure of the evidence-chain benchmark.
- `schema.py`: Defines data classes (Python dataclasses) for the structured, stepwise evidence-chain logs.
- `sample_workflow.json`: Provides a minimal synthetic UI workflow as input to the benchmark harness, two steps, explicit ambiguities.
- `main.py`: Runs the benchmark workflow: loads input, steps through each UI state, simulates agent 'evidence-chain' output, and writes the audit log.
- `output_log.json`: Shows an example of the evidence-chain audit log produced by running the sample workflow (for illustration, not meant to be real audit data).
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.