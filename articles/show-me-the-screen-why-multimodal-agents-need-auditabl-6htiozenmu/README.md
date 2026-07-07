# aetna-research-lab
Benchmark harness for stepwise evidence logging and replay in multimodal agent workflows: screen, intent, action, outcome.
## Article
Show Me the Screen: Why Multimodal Agents Need Auditable Evidence Chains
Trust in multimodal AI agents must be earned by exposing replayable evidence chains, screen, intent, action, and outcome, not just outputting actions.
## Purpose
A public code artifact operationalizes the Screen-Intent-Action-Outcome Replay Benchmark proposed in the Article, allowing others to inspect, test, and extend evidence-chain evaluation, critical for credibility and adoption.
## Generated Notes
Benchmark harness for stepwise evidence logging and replay in multimodal agent workflows: screen, intent, action, outcome.
## Article
Show Me the Screen: Why Multimodal Agents Need Auditable Evidence Chains
Trust in multimodal AI agents must be earned by exposing replayable evidence chains, screen, intent, action, and outcome, not just outputting actions.
## Purpose
A public code artifact operationalizes the Screen-Intent-Action-Outcome Replay Benchmark proposed in the Article, allowing others to inspect, test, and extend evidence-chain evaluation, critical for credibility and adoption.
## Generated Notes
**Purpose**: Prototype benchmark for stepwise evidence-chain logging and replay in multimodal agent workflows. Inspired by the X Article:

"Show Me the Screen: Why Multimodal Agents Need Auditable Evidence Chains"

## What it does
- Defines minimal schema and Python harness for logging and replaying evidence across:
    1. UI screen state (image + UI structure)
    2. Inferred user intent
    3. Agent action and rationale
    4. Outcome (next screen state)
- Loads and replays evidence logs, letting a human or test procedure step through the full episode
- Scores: Is the episode reproducible, debuggable, and attributable from evidence chain?

## Usage
- See the `example_episode.json` for input format
- Run `python replay.py example_episode.json` to step through a replay (text only; UI/screenshot is stand-in here)
- See `schema.py` for the minimal episode data model

## Scope
- This is a minimal reference. No agent is included; use with logs from your own stack or synthetic runs.
- No secrets, APIs, or external dependencies beyond Python stdlib (and Pillow for demo screenshot image load if needed).

## Article:
"Show Me the Screen: Why Multimodal Agents Need Auditable Evidence Chains"

## License
MIT
## Files
- `README.md`: Explains the benchmark purpose, data format, usage instructions, and scope. Users can quickly understand what this repo demonstrates.
- `schema.py`: Defines the benchmark episode data structures for screen state, intent, action, and outcome. Sets the required fields for logs.
- `replay.py`: Console script to replay and inspect an evidence-chain episode. Demonstrates chain visibility, debug, and attribution.
- `example_episode.json`: Shows a minimal example of the evidence log schema for one simple workflow episode.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Explains the benchmark purpose, data format, usage instructions, and scope. Users can quickly understand what this repo demonstrates.
- `schema.py`: Defines the benchmark episode data structures for screen state, intent, action, and outcome. Sets the required fields for logs.
- `replay.py`: Console script to replay and inspect an evidence-chain episode. Demonstrates chain visibility, debug, and attribution.
- `example_episode.json`: Shows a minimal example of the evidence log schema for one simple workflow episode.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.