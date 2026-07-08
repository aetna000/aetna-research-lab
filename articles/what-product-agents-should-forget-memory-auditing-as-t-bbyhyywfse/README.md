# aetna-research-lab
Minimal reference implementation for auditable, replayable memory-step logs in multimodal agent UI workflows.
## Article
What Product Agents Should Forget: Memory Auditing as the Next Multimodal Benchmark
The main hurdle for trustworthy multimodal product agents is not how much memory they have, but whether their persistent state is auditable, attributable, and selectively replayable step by step.
## Purpose
The Article proposes a minimal, auditable memory audit protocol for multimodal agent workflows and claims novelty in operationalizing step-indexed memory-action logs tied to UI state. A reference implementation showing logging, replay, and annotation is necessary to make the Article credible and actionable for builders, researchers, and auditors.
## Generated Notes
Minimal reference implementation for auditable, replayable memory-step logs in multimodal agent UI workflows.
## Article
What Product Agents Should Forget: Memory Auditing as the Next Multimodal Benchmark
The main hurdle for trustworthy multimodal product agents is not how much memory they have, but whether their persistent state is auditable, attributable, and selectively replayable step by step.
## Purpose
The Article proposes a minimal, auditable memory audit protocol for multimodal agent workflows and claims novelty in operationalizing step-indexed memory-action logs tied to UI state. A reference implementation showing logging, replay, and annotation is necessary to make the Article credible and actionable for builders, researchers, and auditors.
## Generated Notes
Reference implementation for the minimal memory-auditing protocol in multimodal agent workflows, as introduced in ‘What Product Agents Should Forget: Memory Auditing as the Next Multimodal Benchmark’.

## Motivation

Multimodal agent stacks default to blob-history, making it hard to trace which persistent memories drive actions, or why context was forgotten/isolate. This repo provides a minimal protocol and simulation for step-indexed, replayable memory-action audit logs, explicitly linking memory add/remove to UI screen state.

## Features
- Logs each workflow step: screen/UI state, memory added/removed, action, and memory-action linkage.
- Attributable provenance for every persisted memory.
- Supports memory redaction/forget with reason, not just accumulation.
- Replay tool for audit and inspection.

## Install & Run
Python 3.8+ only, no dependencies beyond standard library.

```bash
python3 memory_audit_simulate.py
python3 audit_replay.py
```

## Example
See fixture_workflow.json for a sample multi-step agent workflow with memory adds/removes, UI states, and actions, ready for replay and inspection.

## Reference
See ‘What Product Agents Should Forget: Memory Auditing as the Next Multimodal Benchmark’. For contributions and issues, open on https://github.com/aetna000/aetna-research-lab
## Files
- `README.md`: Repository documentation, experiment motivation, usage, and example.
- `memory_audit.py`: Implements the MemoryAuditLog and supporting data classes to record, attribute, and replay stepwise agent memory actions tied to UI state.
- `memory_audit_simulate.py`: Example simulation: logs a three-step agent workflow with add/remove memories, UI state attribution, and action auditing.
- `audit_replay.py`: Replay and inspect each step in a memory-audited workflow log for audit, benchmarking, and debugging.
- `fixture_workflow.json`: Synthetic, pre-logged agent workflow: 3 steps with memory adds/removes, UI states, and stepwise audit log.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Repository documentation, experiment motivation, usage, and example.
- `memory_audit.py`: Implements the MemoryAuditLog and supporting data classes to record, attribute, and replay stepwise agent memory actions tied to UI state.
- `memory_audit_simulate.py`: Example simulation: logs a three-step agent workflow with add/remove memories, UI state attribution, and action auditing.
- `audit_replay.py`: Replay and inspect each step in a memory-audited workflow log for audit, benchmarking, and debugging.
- `fixture_workflow.json`: Synthetic, pre-logged agent workflow: 3 steps with memory adds/removes, UI states, and stepwise audit log.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.