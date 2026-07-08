# aetna-research-lab
Minimal, public benchmark for stepwise evidence-chain logging in multimodal agent workflows (screen, intent, action, outcome, evidence, and replay).
## Article
The Benchmark Multimodal Agents Can’t Fake: Minimal UI Evidence Chains or Bust
The only credible benchmark for trustworthy multimodal agents in real workflows is a replayable, auditor-facing evidence-chain log, screen, intent, action, and outcome, stepwise for each task.
## Purpose
The Article proposes a minimal, replayable benchmark evaluating whether multimodal agents expose auditable evidence chains through stepwise UI workflows. No such open-source harness or schema exists in prior work. A minimal repo containing benchmark harness, task schema, evaluation workflow, and example artifacts will make the proposal credible and actionable for other researchers and practitioners.
## Generated Notes
Minimal, public benchmark for stepwise evidence-chain logging in multimodal agent workflows (screen, intent, action, outcome, evidence, and replay).
## Article
The Benchmark Multimodal Agents Can’t Fake: Minimal UI Evidence Chains or Bust
The only credible benchmark for trustworthy multimodal agents in real workflows is a replayable, auditor-facing evidence-chain log, screen, intent, action, and outcome, stepwise for each task.
## Purpose
The Article proposes a minimal, replayable benchmark evaluating whether multimodal agents expose auditable evidence chains through stepwise UI workflows. No such open-source harness or schema exists in prior work. A minimal repo containing benchmark harness, task schema, evaluation workflow, and example artifacts will make the proposal credible and actionable for other researchers and practitioners.
## Generated Notes
Minimal, open-source benchmark for testing whether multimodal agents log and justify each step through a UI workflow: screen, intent, action, outcome, and explicit evidence chain.

## Why?
Nearly every agent stack claims autonomy. Few can replay a workflow, screen by screen, and explain, with concrete evidence, what they saw, intended, did, and why. This repo provides a baseline harness and schema for evaluating that claim with minimal synthetic UI tasks.

## What does it do?
- Loads a small sequence of synthetic UI screens (images or schema).
- At each step, challenges agent to:
    1. Parse and log screen state (elements, text, ambiguity).
    2. Infer and record intent (with evidence reference).
    3. Propose and justify action (anchored to screen/UI region).
    4. Log outcome/result after simulated execution.
    5. Output full evidence-chain trace usable for audit/replay.
- Provides baseline evaluation scripts to check attribution links and replay audibility.

## Files
- `schema.py`: Stepwise evidence-chain data structure & validation
- `tasks/example_task.json`: Synthetic UI workflow definition
- `agent_stub.py`: Minimal agent API; replace with your own logic
- `run_benchmark.py`: Loads task, iterates workflow, compiles logged trace
- `evaluate_trace.py`: Checks evidence chain integrity and attribution coverage

## Quickstart
```
python run_benchmark.py tasks/example_task.json output/example_trace.json
python evaluate_trace.py output/example_trace.json
```

## Extending
- Add real or synthetic UI tasks to `tasks/`.
- Plug in your own agent logic via `agent_stub.py` or swap in a real model.
- Use `evaluate_trace.py` to audit outputs for missing/weak evidence chains.

## Reference
Cited in: “The Benchmark Multimodal Agents Can’t Fake: Minimal UI Evidence Chains or Bust” (@aetna000, 2024)
## Files
- `README.md`: Explains the purpose, setup, workflow, file structure, and how to use or extend the benchmark.
- `schema.py`: Defines the evidence-chain trace schema and validates logged agent output for replay and audit.
- `tasks/example_task.json`: Defines a minimal synthetic UI workflow for the agent to process and log evidence chains against.
- `agent_stub.py`: Provides a placeholder agent function that processes each UI screen, simulates decision, and logs evidence per step.
- `run_benchmark.py`: Orchestrates the benchmark: loads a workflow, runs each screen through the agent, saves stepwise evidence-chain trace.
- `evaluate_trace.py`: Checks a generated trace for schema compliance and minimal evidence chain coverage (for each step: evidence for intent/action, attribution present).
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Explains the purpose, setup, workflow, file structure, and how to use or extend the benchmark.
- `schema.py`: Defines the evidence-chain trace schema and validates logged agent output for replay and audit.
- `tasks/example_task.json`: Defines a minimal synthetic UI workflow for the agent to process and log evidence chains against.
- `agent_stub.py`: Provides a placeholder agent function that processes each UI screen, simulates decision, and logs evidence per step.
- `run_benchmark.py`: Orchestrates the benchmark: loads a workflow, runs each screen through the agent, saves stepwise evidence-chain trace.
- `evaluate_trace.py`: Checks a generated trace for schema compliance and minimal evidence chain coverage (for each step: evidence for intent/action, attribution present).
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.