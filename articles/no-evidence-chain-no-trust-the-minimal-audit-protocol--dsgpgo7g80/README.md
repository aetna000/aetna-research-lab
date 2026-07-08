# aetna-research-lab
Minimal evidence-chain (SIAO) benchmark for trustworthy multimodal agent stepwise replay: screen, intent, action, outcome.
## Article
No Evidence Chain, No Trust: The Minimal Audit Protocol Product AI Agents Can’t Fake
Product-worthy multimodal agents must expose a stepwise, replayable evidence chain, screen, intent, action, and outcome, at every workflow step, and most do not.
## Purpose
The Article's thesis is a minimal, actionable benchmark for agent evidence-chain auditability (SIAO protocol). A reference repo makes this real, so anyone can inspect or extend the logging protocol, dataset schema, and replay logic. This directly supports the credibility and utility of the Article, moving it from theory to a public artifact for benchmarking and critique.
## Generated Notes
Minimal evidence-chain (SIAO) benchmark for trustworthy multimodal agent stepwise replay: screen, intent, action, outcome.
## Article
No Evidence Chain, No Trust: The Minimal Audit Protocol Product AI Agents Can’t Fake
Product-worthy multimodal agents must expose a stepwise, replayable evidence chain, screen, intent, action, and outcome, at every workflow step, and most do not.
## Purpose
The Article's thesis is a minimal, actionable benchmark for agent evidence-chain auditability (SIAO protocol). A reference repo makes this real, so anyone can inspect or extend the logging protocol, dataset schema, and replay logic. This directly supports the credibility and utility of the Article, moving it from theory to a public artifact for benchmarking and critique.
## Generated Notes
Reference implementation of the SIAO (Screen, Intent, Action, Outcome) stepwise evidence protocol for trustworthy multimodal agent benchmarking.

## Purpose
Enables audit and replay of agent decisions by logging, for every workflow step:
1. Pre-action screen state (screenshot path and parsed UI elements)
2. Parsed UI elements and ambiguities
3. Explicit intent statement with evidence
4. Selected action and rationale
5. Post-action outcome (screen diff or state change)

Each step forms a link in a replayable chain. Missing any link breaks the chain and auditability.

## Usage
- Use the SIAO schema (see `siao_schema.py`) to log each workflow step.
- The example runner (`example_run.py`) demonstrates logging a 3-step toy UI workflow.
- All logs are serialized as JSON for inspection.

## Article
Implements benchmark in: *No Evidence Chain, No Trust: The Minimal Audit Protocol Product AI Agents Can’t Fake* (@aetna000)

## Sources
See References in the corresponding X Article.
## Files
- `README.md`: Docs: Describes the purpose, SIAO protocol, usage, and schema of the benchmark.
- `siao_schema.py`: Defines the minimal SIAO evidence-chain log schema and serialization utilities.
- `example_run.py`: Demo: Simulates a simple 3-step UI workflow and logs a SIAO evidence chain.
- `example_trace.json`: Sample output: Replayable evidence chain from the example run, for inspection and benchmarking.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Docs: Describes the purpose, SIAO protocol, usage, and schema of the benchmark.
- `siao_schema.py`: Defines the minimal SIAO evidence-chain log schema and serialization utilities.
- `example_run.py`: Demo: Simulates a simple 3-step UI workflow and logs a SIAO evidence chain.
- `example_trace.json`: Sample output: Replayable evidence chain from the example run, for inspection and benchmarking.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.