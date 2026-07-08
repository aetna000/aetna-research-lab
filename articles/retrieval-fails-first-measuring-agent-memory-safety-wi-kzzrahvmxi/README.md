# aetna-research-lab
Reference ARRB harness for measuring agent memory safety via adversarial recall, not storage logs. Includes schema, scoring, and example workflow.
## Article
Retrieval Fails First: Measuring Agent Memory Safety with Adversarial Recall, Not Storage Logs
Memory safety for product AI agents must be measured not by storage logs but by adversarial retrieval: how reliably agents recall, reject, or isolate critical memory elements, under attack, ambiguity, and workflow complexity.
## Purpose
The Article advances a concrete adversarial recall benchmark (ARRB) and methodology. A compact, public repo with a minimal harness, score script, and schema makes this proposal credible, reusable, and inspectable, supporting adoption and critical review.
## Generated Notes
Reference ARRB harness for measuring agent memory safety via adversarial recall, not storage logs. Includes schema, scoring, and example workflow.
## Article
Retrieval Fails First: Measuring Agent Memory Safety with Adversarial Recall, Not Storage Logs
Memory safety for product AI agents must be measured not by storage logs but by adversarial retrieval: how reliably agents recall, reject, or isolate critical memory elements, under attack, ambiguity, and workflow complexity.
## Purpose
The Article advances a concrete adversarial recall benchmark (ARRB) and methodology. A compact, public repo with a minimal harness, score script, and schema makes this proposal credible, reusable, and inspectable, supporting adoption and critical review.
## Generated Notes
ARRB is a minimal, reference harness for empirically auditing agent memory safety via adversarial recall, as proposed in the X Article 'Retrieval Fails First: Measuring Agent Memory Safety with Adversarial Recall, Not Storage Logs'.

**Why?**
- Storage logs alone miss the real product risk: what agents actually recall or misrecall during messy workflows, especially under attack.
- Adversarial recall testing injects ambiguous, revoked, or cross-session memory and traces what agents leak, forget, or blend.
- This repo provides:
  * A generic input schema for workflow/adversarial recall traces
  * Scoring script for false recall and recall-miss rates
  * Example test input/fixture

**How to use**
- Populate `example_trace.json` with workflow traces (one per agent episode/step, annotated by recall type, ground truth, and retrieved memory)
- Run `score_recall.py` to compute error rates per workflow or agent
- Extend for your agent stack or dataset

**Citations**
- Article: 'Retrieval Fails First: Measuring Agent Memory Safety with Adversarial Recall, Not Storage Logs' (Aetna)
- See README References for foundational research

**License**: MIT (no warranty)
## Files
- `README.md`: Explain ARRB motivation, design, schema, and usage. Show how this supports the Article and enables reproducible recall/error experiments.
- `arrb_schema.py`: Defines the minimal Python dict/JSON schema for an ARRB trace episode: inputs, adversarial memory, observed agent output, annotations.
- `score_recall.py`: Implements scoring of false recall and recall miss rates from a list of ARRB episode JSONs.
- `example_trace.json`: Provides a compact, readable sample of adversarial ARRB test episodes with ground truth, agent recalls, for reproducible demonstration and testing.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Explain ARRB motivation, design, schema, and usage. Show how this supports the Article and enables reproducible recall/error experiments.
- `arrb_schema.py`: Defines the minimal Python dict/JSON schema for an ARRB trace episode: inputs, adversarial memory, observed agent output, annotations.
- `score_recall.py`: Implements scoring of false recall and recall miss rates from a list of ARRB episode JSONs.
- `example_trace.json`: Provides a compact, readable sample of adversarial ARRB test episodes with ground truth, agent recalls, for reproducible demonstration and testing.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.