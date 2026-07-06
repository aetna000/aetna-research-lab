# aetna-research-lab
Reference implementation for I Do Not Trust Screen Agents Without a Trace
## Article
I Do Not Trust Screen Agents Without a Trace
The product bottleneck for multimodal agents is not action generation; it is evidence that makes the action trustworthy.
## Purpose
The Article proposes an algorithmic evaluation method that benefits from a small reference implementation.
## Generated Notes
Reference implementation for I Do Not Trust Screen Agents Without a Trace
## Article
I Do Not Trust Screen Agents Without a Trace
The product bottleneck for multimodal agents is not action generation; it is evidence that makes the action trustworthy.
## Purpose
The Article proposes an algorithmic evaluation method that benefits from a small reference implementation.
## Generated Notes
Research prototype for an Aetna X Article.

This repository contains a minimal evidence-chain evaluator for trustworthy multimodal agent workflows. It does not prove an agent is safe. It gives researchers and builders a small starting point for recording what an agent saw, what it inferred, what it did, and what changed.

## Run

```bash
python3 evidence_chain_eval.py examples/sample_trace.json
```

## Files

- `evidence_chain_eval.py`: scores a JSON action trace for evidence completeness.
- `examples/sample_trace.json`: toy trace format.

## Status

Research prototype. Review and adapt before using in production.
## Files
- `README.md`: Repository overview and run instructions.
- `evidence_chain_eval.py`: Minimal evidence-chain scoring script.
- `examples/sample_trace.json`: Toy example of the evidence-chain trace schema.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Repository overview and run instructions.
- `evidence_chain_eval.py`: Minimal evidence-chain scoring script.
- `examples/sample_trace.json`: Toy example of the evidence-chain trace schema.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.