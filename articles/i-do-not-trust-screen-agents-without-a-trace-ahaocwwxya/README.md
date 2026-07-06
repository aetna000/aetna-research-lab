# aetna-research-lab
Reference code for evidence-chain evaluation: tracing screen, intent, action, and outcome for trustworthy multimodal agents.
## Article
I Do Not Trust Screen Agents Without a Trace
The product bottleneck for multimodal agents is not action generation; it is evidence that makes the action trustworthy.
## Purpose
The Article proposes an evidence-chain evaluation benchmark for multimodal screen agents, specifying a concrete evaluation method (capture UI state, infer intent, cite evidence, record action, and compare post-action outcome). To build trust and give readers a real inspection target, a minimal public code artifact is warranted: a harness that logs each step, structures the evidence chain, and simulates at least one dummy agent action with replayable evidence trace. No claims of end-to-end produc
## Generated Notes
Reference code for evidence-chain evaluation: tracing screen, intent, action, and outcome for trustworthy multimodal agents.
## Article
I Do Not Trust Screen Agents Without a Trace
The product bottleneck for multimodal agents is not action generation; it is evidence that makes the action trustworthy.
## Purpose
The Article proposes an evidence-chain evaluation benchmark for multimodal screen agents, specifying a concrete evaluation method (capture UI state, infer intent, cite evidence, record action, and compare post-action outcome). To build trust and give readers a real inspection target, a minimal public code artifact is warranted: a harness that logs each step, structures the evidence chain, and simulates at least one dummy agent action with replayable evidence trace. No claims of end-to-end produc
## Files
- `articles/i-do-not-trust-screen-agents-without-a-trace-ahaocwwxya/README.md`: Explain the benchmark harness, usage, and evaluation flow for evidence-chain logging.
- `articles/i-do-not-trust-screen-agents-without-a-trace-ahaocwwxya/evidence_chain.py`: Implements the minimal evidence-chain evaluation harness as described in the Article.
- `articles/i-do-not-trust-screen-agents-without-a-trace-ahaocwwxya/example_fixture.json`: Provides a fixture for a pre-action UI screen state for the harness to consume.
- `articles/i-do-not-trust-screen-agents-without-a-trace-ahaocwwxya/chain_log_example.json`: Shows a sample output of a complete evidence-chain log for one agent step.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `articles/i-do-not-trust-screen-agents-without-a-trace-ahaocwwxya/README.md`: Explain the benchmark harness, usage, and evaluation flow for evidence-chain logging.
- `articles/i-do-not-trust-screen-agents-without-a-trace-ahaocwwxya/evidence_chain.py`: Implements the minimal evidence-chain evaluation harness as described in the Article.
- `articles/i-do-not-trust-screen-agents-without-a-trace-ahaocwwxya/example_fixture.json`: Provides a fixture for a pre-action UI screen state for the harness to consume.
- `articles/i-do-not-trust-screen-agents-without-a-trace-ahaocwwxya/chain_log_example.json`: Shows a sample output of a complete evidence-chain log for one agent step.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.