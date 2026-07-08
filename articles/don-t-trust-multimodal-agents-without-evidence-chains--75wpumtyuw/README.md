# aetna-research-lab
Minimal reference code for benchmarking evidence chains in multimodal screen agents: stepwise logs of screen state, intent, action, and outcome.
## Article
Don’t Trust Multimodal Agents Without Evidence Chains: The Real Product Bottleneck
The product bottleneck for multimodal agents is not action generation; it is stepwise evidence that justifies every action.
## Purpose
The Article proposes a concrete 'evidence-chain benchmark' for multimodal agents, requiring stepwise logs of screen, intent, action, and outcome. A minimal public code artifact, a reference implementation of the evidence-chain logging protocol and a harness for evaluating agent traces, makes the proposal actionable, inspectable, and testable by other researchers and product teams. Without it, the benchmark claim is just theory.
## Generated Notes
Minimal reference code for benchmarking evidence chains in multimodal screen agents: stepwise logs of screen state, intent, action, and outcome.
## Article
Don’t Trust Multimodal Agents Without Evidence Chains: The Real Product Bottleneck
The product bottleneck for multimodal agents is not action generation; it is stepwise evidence that justifies every action.
## Purpose
The Article proposes a concrete 'evidence-chain benchmark' for multimodal agents, requiring stepwise logs of screen, intent, action, and outcome. A minimal public code artifact, a reference implementation of the evidence-chain logging protocol and a harness for evaluating agent traces, makes the proposal actionable, inspectable, and testable by other researchers and product teams. Without it, the benchmark claim is just theory.
## Generated Notes
This repository provides a minimal reference implementation of the evidence-chain benchmark protocol for multimodal agents that act on UIs/screens. The goal is to enable research and product teams to:

- Enforce and evaluate stepwise logging of four audit artifacts: pre-action screen state, inferred intent (with evidence), chosen action/rationale, and post-action outcome.
- Diagnose breakdowns (UI grounding, intent inference, planning, evidence, or tool error) in product workflows.
- Benchmark and debug agents for trustworthiness, not just task completion.

**Why:** If an agent can't show what it saw and why it acted, it's not product ready. See [Pix2Struct](https://arxiv.org/abs/2210.03347), [PROV-AGENT](http://arxiv.org/abs/2508.02866v3), [CraniMem](https://arxiv.org/abs/2309.03347).

## Key Components
- `evidence_schema.py`: Defines the evidence chain data structure.
- `trace_logger.py`: Reference logger for agent actions per the benchmark protocol.
- `example_workflow.py`: Example usage simulating an agent workflow on a minimal synthetic UI.
- `fixtures/example_ui_state.json`: Sample UI state for demonstration.

## Usage
1. Define workflow steps as sequences of UI states.
2. For each step, call the logger to record:
    - pre-action screen state
    - inferred intent with evidence
    - selected action & rationale
    - post-action outcome (synthetic or real)
3. The logger outputs a replayable JSON trace for audit.

## Example
Run: `python example_workflow.py`

Outputs stepwise evidence trace for a toy workflow.

This code is for research and benchmarking only: no secrets or product dependencies included.
## Files
- `README.md`: Summarizes the benchmark goal, evidence chain schema, usage instructions, and research context.
- `evidence_schema.py`: Defines the evidence-chain log data structure per Article's minimal protocol.
- `trace_logger.py`: Reference harness for building and saving evidence-chain traces through a workflow.
- `example_workflow.py`: Runs a toy workflow logging stepwise evidence for a synthetic UI, showing how to use the protocol.
- `fixtures/example_ui_state.json`: Synthetic, minimal list of UI screen states for the toy workflow in example_workflow.py.
- `fixtures/example_run_trace.json`: Output artifact: sample trace of a simulated two-step agent workflow using the evidence-chain protocol.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Summarizes the benchmark goal, evidence chain schema, usage instructions, and research context.
- `evidence_schema.py`: Defines the evidence-chain log data structure per Article's minimal protocol.
- `trace_logger.py`: Reference harness for building and saving evidence-chain traces through a workflow.
- `example_workflow.py`: Runs a toy workflow logging stepwise evidence for a synthetic UI, showing how to use the protocol.
- `fixtures/example_ui_state.json`: Synthetic, minimal list of UI screen states for the toy workflow in example_workflow.py.
- `fixtures/example_run_trace.json`: Output artifact: sample trace of a simulated two-step agent workflow using the evidence-chain protocol.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.