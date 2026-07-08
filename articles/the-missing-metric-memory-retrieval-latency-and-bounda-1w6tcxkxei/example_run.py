from mrlba_harness import MemoryFragment, MRLBAHarness
import time

mem_store = [
    MemoryFragment("reset user password", "alice", "sess1", "screenA", 1717100000.0),
    MemoryFragment("set server config", "bob", "sess2", "screenB", 1717101000.0),
    MemoryFragment("set theme", "alice", "sess1", "screenC", 1717102000.0)
]

harness = MRLBAHarness(mem_store)

queries = [
    {"content": "reset user password", "type": "in-scope"},
    {"content": "set server config", "type": "out-of-scope"},
    {"content": "nonexistent fragment", "type": "distractor"}
]

# Alice logs in to sess1 and issues queries
for q in queries:
    log = harness.retrieve(q, current_user="alice", current_session="sess1")
    print(f"[MRLBA] Retrieval: {log.query}, Latency: {log.latency_ms} ms, Boundary Violation: {log.boundary_violation}, Type: {log.violation_type}")

harness.save_audit_log("data/audit_trace.jsonl")