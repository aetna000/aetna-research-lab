import time
from datetime import datetime
from worba_schema import AuditRun, AuditStep, RetrievalEvent, Provenance, BoundaryScope, AuditScore

class SimpleMemoryStore:
    def __init__(self):
        # key: (user_id, session_id, tool_id)
        self.memory = {}
    def add(self, user, session, tool, text, source):
        k = (user, session, tool)
        self.memory[k] = {'text': text, 'provenance': source, 'timestamp': datetime.utcnow().isoformat()}
    def retrieve(self, user, session, tool):
        k = (user, session, tool)
        if k in self.memory:
            entry = self.memory[k]
            return entry['text'], Provenance(user, session, tool, entry['provenance'], entry['timestamp'])
        return None, None

class SyntheticAgent:
    def __init__(self, store: SimpleMemoryStore):
        self.store = store
    def retrieve_memory(self, user, session, tool):
        return self.store.retrieve(user, session, tool)

# For simplicity: 3 steps, users A and B, sessions x and y, one tool.
def run_synthetic_worba_audit():
    memory = SimpleMemoryStore()
    # Step 1: User A, session x, tool T
    memory.add('A', 'x', 'T', 'UserA SessionX Note1', 'chat_log')
    # Step 2: User B, session y, tool T
    memory.add('B', 'y', 'T', 'UserB SessionY Note1', 'chat_log')
    agent = SyntheticAgent(memory)

    steps = []
    # Step 1: user A, session x
    in_scope = agent.retrieve_memory('A', 'x', 'T')
    out_scope = agent.retrieve_memory('B', 'y', 'T')  # Should not retrieve A's memory
    ambiguous = agent.retrieve_memory('A', 'y', 'T')  # Ambiguous: same user, different session
    ret_events = []
    now = datetime.utcnow().isoformat()
    def make_event(query, scope, retrieved, prov, match, leak, ambiguous_p):
        start = now
        finish = now
        return RetrievalEvent(
            query=query,
            query_scope=scope,
            query_start=start,
            retrieval_finish=finish,
            retrieved_memory=retrieved,
            provenance=prov,
            boundary_match=match,
            leak_detected=leak,
            ambiguous_provenance=ambiguous_p,
            latency_ms=0
        )
    ret_events.append(make_event('Recall own note', BoundaryScope.IN_SCOPE, in_scope[0], in_scope[1], True, False, False))
    ret_events.append(make_event('Recall other user note', BoundaryScope.OUT_OF_SCOPE, out_scope[0], out_scope[1], False, bool(out_scope[0]), False))
    ret_events.append(make_event('Recall ambiguous session', BoundaryScope.AMBIGUOUS, ambiguous[0], ambiguous[1], False, False, True))
    audit_score = AuditScore.SAFE if all(e.boundary_match and not e.leak_detected for e in ret_events if e.query_scope == BoundaryScope.IN_SCOPE) else AuditScore.FAIL
    anomaly_flags = ["leak"] if any(e.leak_detected for e in ret_events) else []
    steps.append(AuditStep(1, "UserA, SessionX, ToolT", "A", "x", "T", ret_events, audit_score, anomaly_flags))

    # Step 2: user B, session y
    now = datetime.utcnow().isoformat()
    in_scope = agent.retrieve_memory('B', 'y', 'T')
    out_scope = agent.retrieve_memory('A', 'x', 'T')
    ambiguous = agent.retrieve_memory('B', 'x', 'T')
    ret_events = []
    ret_events.append(make_event('Recall own note', BoundaryScope.IN_SCOPE, in_scope[0], in_scope[1], True, False, False))
    ret_events.append(make_event('Recall other user note', BoundaryScope.OUT_OF_SCOPE, out_scope[0], out_scope[1], False, bool(out_scope[0]), False))
    ret_events.append(make_event('Recall ambiguous session', BoundaryScope.AMBIGUOUS, ambiguous[0], ambiguous[1], False, False, True))
    audit_score = AuditScore.SAFE if all(e.boundary_match and not e.leak_detected for e in ret_events if e.query_scope == BoundaryScope.IN_SCOPE) else AuditScore.FAIL
    anomaly_flags = ["leak"] if any(e.leak_detected for e in ret_events) else []
    steps.append(AuditStep(2, "UserB, SessionY, ToolT", "B", "y", "T", ret_events, audit_score, anomaly_flags))

    # Step 3: Simulate failure: user B, session y tries to retrieve A's memory
    now = datetime.utcnow().isoformat()
    ret_event = make_event(
        'Malicious recall: try to fetch UserA note',
        BoundaryScope.OUT_OF_SCOPE,
        agent.retrieve_memory('A', 'x', 'T')[0],
        agent.retrieve_memory('A', 'x', 'T')[1],
        False,
        True,
        False
    )
    steps.append(AuditStep(3, "UserB, SessionY, ToolT", "B", "y", "T", [ret_event], AuditScore.FAIL, ["leak"]))

    run_time = datetime.utcnow().isoformat()
    trustworthy = all(s.audit_score == AuditScore.SAFE for s in steps)
    run = AuditRun("synthetic_demo_workflow", steps, trustworthy, run_time)
    return run