# aetna-research-lab
Reference implementation of the audit card scoring for agent workflow boundary failures, accompanying the article on workflow benchmarks and evaluation design.
## Article
A Small Benchmark for Agent Boundary Failures After Lost in the Middle: How Language Mo...
The product bottleneck for workflow benchmarks and evaluation design is not only model capability; it is whether each boundary in the agent step can be audited.
## Purpose
A minimal reference implementation of the audit card scoring algorithm adds credibility to the article's proposed boundary audit method, allowing researchers and builders to inspect and adapt the scoring logic.
## Generated Notes
Reference implementation of the audit card scoring for agent workflow boundary failures, accompanying the article on workflow benchmarks and evaluation design.
## Article
A Small Benchmark for Agent Boundary Failures After Lost in the Middle: How Language Mo...
The product bottleneck for workflow benchmarks and evaluation design is not only model capability; it is whether each boundary in the agent step can be audited.
## Purpose
A minimal reference implementation of the audit card scoring algorithm adds credibility to the article's proposed boundary audit method, allowing researchers and builders to inspect and adapt the scoring logic.
## Generated Notes
Reference implementation of the audit card scoring algorithm proposed in the research article "A Small Benchmark for Agent Boundary Failures After Lost in the Middle: How Language Models Use Long Contexts".

## Usage

```bash
python audit_card.py example_trace.json
```

The script reads a JSON file containing a list of agent workflow steps and outputs a scoring report with per-step boundary failure flags and an overall boundary pass rate.

## Step Schema

Each step in the input trace should contain these fields:

- `claim`: The user-visible claim or action.
- `evidence_type`: One of `observation`, `inference`, `preference`, `instruction`, `permission`, `outcome`.
- `evidence_source`: Where the evidence came from (e.g., UI element, memory key).
- `action_justified`: The smallest action justified by the evidence.
- `expected_outcome`: What should happen.
- `post_action_observation`: What actually happened.
- (Optional) `permission_boundary`, `memory_scope`, `memory_access_permission`, `stale_state_flag`, `memory_age_seconds`, `intent_verification`.

## Boundary Failure Categories

- `missing_evidence`: No evidence source provided.
- `stale_state`: Memory or state used may be outdated.
- `ambiguous_intent`: Preference used without explicit verification.
- `permission_gap`: High-risk action without clear permission grounding.
- `unverifiable_outcome`: Post-action observation does not match expected outcome.
- `over_broad_memory`: Global memory accessed without explicit permission.

## Limitations

This is a research prototype. The scoring heuristics (e.g., high-risk keyword detection, age threshold) are illustrative and not production-ready. Teams should tailor the rules to their own workflow domains.
## Files
- `audit_card.py`: Core implementation of the audit card scoring algorithm described in the article.
- `example_trace.json`: Example workflow trace with steps annotated for audit card scoring.
- `README.md`: Documentation for the repository, linking to the article and explaining usage.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `audit_card.py`: Core implementation of the audit card scoring algorithm described in the article.
- `example_trace.json`: Example workflow trace with steps annotated for audit card scoring.
- `README.md`: Documentation for the repository, linking to the article and explaining usage.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.