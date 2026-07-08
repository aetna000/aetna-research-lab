# aetna-research-lab
Minimal benchmark harness for the Forgetting Audit Protocol: test and log AI agent intentional forgetting at session, user, or policy boundaries.
## Article
Memory Safety Isn’t Enough: Benchmarking What Agents Should Forget, Not Just What They Retrieve
Trustworthy agents must prove not just what they retrieve, but what they can intentionally and reliably forget, measured via adversarial forgetting benchmarks that log when and how forgotten state becomes irretrievable.
## Purpose
This Article proposes the Forgetting Audit Protocol (FAP), an adversarial benchmark for intentional forgetting in AI agents. Credibility and practical value are increased by providing a minimal, inspectable FAP harness for empirical tests, demonstrating how agents should be probed for memory erasure at workflow boundaries.
## Generated Notes
Minimal benchmark harness for the Forgetting Audit Protocol: test and log AI agent intentional forgetting at session, user, or policy boundaries.
## Article
Memory Safety Isn’t Enough: Benchmarking What Agents Should Forget, Not Just What They Retrieve
Trustworthy agents must prove not just what they retrieve, but what they can intentionally and reliably forget, measured via adversarial forgetting benchmarks that log when and how forgotten state becomes irretrievable.
## Purpose
This Article proposes the Forgetting Audit Protocol (FAP), an adversarial benchmark for intentional forgetting in AI agents. Credibility and practical value are increased by providing a minimal, inspectable FAP harness for empirical tests, demonstrating how agents should be probed for memory erasure at workflow boundaries.
## Generated Notes
This repository provides a minimal reference implementation of the Forgetting Audit Protocol (FAP): a reproducible benchmark and test harness for probing intentional forgetting (deletion, expiry, boundary-triggered erasure) in product-grade AI agents.

## Purpose
FAP adversarially tests AI memory systems: after an agent claims to forget something (session end, user switch, permission change), the harness probes whether forgotten data can be recovered, referenced, or leaks via embeddings.

- **Active Forgetting:** Explicit deletions after workflow or policy events
- **Passive Forgetting:** Time-based expiry/decay; checks for persistent leakage

## Protocol Steps
1. Define _forgetting events_ (session/user/permission boundary, policy wipe).
2. Log memory items added before boundaries.
3. Trigger boundary; instruct agent to forget the target items.
4. Probe the agent post-boundary for forgotten data by direct and indirect means.
5. Record results: retrieval success/fail, leakage via surrogate probes, reliquification from embeddings.

## Usage
- Implement or wrap your agent using the `AgentInterface` defined in `fap_harness.py`.
- Register forgetting events and probe sets.
- Run the benchmark. Inspect the logs for pass/fail by item, boundary, and probe mode.

## Example
See `examples/basic_fap_run.py` for a minimal end-to-end run.

## Limitations
- Synthetic agent and basic probes; intended for harnessing real agent stacks (LangChain, OSS, etc.)
- No secret keys or credentials needed; this is a research prototype.

## Article reference
This code artifact supports the Article _"Memory Safety Isn’t Enough: Benchmarking What Agents Should Forget, Not Just What They Retrieve"_ (Aetna, 2024) and should be cited as such.
## Files
- `README.md`: Explain the protocol, use case, and provide usage instructions for the benchmark harness.
- `fap_harness.py`: Defines the core Forgetting Audit Protocol test harness and agent interface.
- `examples/basic_fap_run.py`: Shows a complete example: Agent stores secret, forgets at a boundary, audit checks retrieval and embedding leak.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Explain the protocol, use case, and provide usage instructions for the benchmark harness.
- `fap_harness.py`: Defines the core Forgetting Audit Protocol test harness and agent interface.
- `examples/basic_fap_run.py`: Shows a complete example: Agent stores secret, forgets at a boundary, audit checks retrieval and embedding leak.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.