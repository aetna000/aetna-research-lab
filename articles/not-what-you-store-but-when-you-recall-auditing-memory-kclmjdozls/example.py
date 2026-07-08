"""
Example: RBA protocol on a simulated agent workflow.
"""

from rba import RetrievalEvent, AuditLog, AuditScorer, Outcome
import time

# Create a session log
log = AuditLog(session_id="sess_01", agent_id="agent_x")

# Step 1: in-scope retrieval, correct
log.add_event(RetrievalEvent(
    step_id="step_1",
    timestamp=time.time(),
    query="user123 order history last 7 days",
    intended_scope={"user_id": "123", "session_id": "sess_01"},
    provenance={"source": "order_db", "table": "orders", "index": "user_id"},
    latency_ms=45.2,
    outcome=Outcome.HIT
))

# Step 2: cross-boundary leak (retrieved another user's data accidentally)
log.add_event(RetrievalEvent(
    step_id="step_2",
    timestamp=time.time(),
    query="user456 payment methods",
    intended_scope={"user_id": "123", "session_id": "sess_01"},
    provenance={"source": "payment_cache", "key": "user456_payment"},
    latency_ms=30.1,
    outcome=Outcome.CROSS_BOUNDARY,
    notes="Retrieved data for user456 despite active user123. Boundary error."
))

# Step 3: omission with justification
log.add_event(RetrievalEvent(
    step_id="step_3",
    timestamp=time.time(),
    query="deleted items from basket",
    intended_scope={"user_id": "123", "session_id": "sess_01"},
    provenance={"source": "none"},
    latency_ms=0.0,
    outcome=Outcome.OMITTED,
    notes="Basket clear policy, no retrieval needed (justified)."
))

# Score
scorer = AuditScorer(log)
print("RBA Audit Report:")
print(scorer.report())

# Export trace
log.export("session_sess_01_audit.json")
print("Exported log to session_sess_01_audit.json")