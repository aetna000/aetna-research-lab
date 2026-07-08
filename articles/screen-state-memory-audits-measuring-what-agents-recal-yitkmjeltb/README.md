# aetna-research-lab
Minimal prototype of Screen-State Memory Audit (SSMA) protocol for agent memory safety.
## Article
Screen-State Memory Audits: Measuring What Agents Recall, Omit, and Miss Across UI Workflows
A product-safe AI agent is defined not by how much it stores, but by whether every memory retrieval is grounded in current screen/UI evidence and can explicitly justify what it omits or fails to recall.
## Purpose
The SSMA protocol requires a concrete reference implementation to illustrate the logging and scoring steps, making the article's proposal executable and testable.
## Generated Notes
Minimal prototype of Screen-State Memory Audit (SSMA) protocol for agent memory safety.
## Article
Screen-State Memory Audits: Measuring What Agents Recall, Omit, and Miss Across UI Workflows
A product-safe AI agent is defined not by how much it stores, but by whether every memory retrieval is grounded in current screen/UI evidence and can explicitly justify what it omits or fails to recall.
## Purpose
The SSMA protocol requires a concrete reference implementation to illustrate the logging and scoring steps, making the article's proposal executable and testable.
## Generated Notes
This repository contains a minimal reference implementation of the Screen-State Memory Audit (SSMA) protocol described in the X Article: "Screen-State Memory Audits: Measuring What Agents Recall, Omit, and Miss Across UI Workflows".

The script `ssma.py` demonstrates how to:
- Capture a simplified screen state (a dictionary of UI elements) at each workflow step.
- Log an agent's memory retrieval attempts, including provenance and intentional omissions.
- Compare retrievals and omissions against a ground-truth gold standard.
- Score per-step retrieval precision, recall, and omission correctness.

This is not a full agent stack; it is a research prototype that illustrates the core logging and scoring logic of SSMA. Run it with:

```bash
python ssma.py
```

No external dependencies are required.
## Files
- `README.md`: Explain the SSMA prototype, how to run it, and its role in the article.
- `ssma.py`: Implement the SSMA logging and scoring logic with a simulated workflow.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.
## Files
- `README.md`: Explain the SSMA prototype, how to run it, and its role in the article.
- `ssma.py`: Implement the SSMA logging and scoring logic with a simulated workflow.
## Status
Research prototype. It is public for inspection, critique, and reuse. It should not be treated as production safety proof without independent validation.