import time
from audit_logging import RetrievalLogger, RetrievalEvent
from audit_scoring import aggregate_score, summarize_boundary_errors, summarize_latency_breaches

def simulate_agent_workflow():
    logger = RetrievalLogger()
    t0 = time.time()
    # Event 1: correct retrieval, in user/session boundary
    logger.log(RetrievalEvent(
        query='find latest invoice for user 123',
        intended_boundary='user',
        provenance='doc_987',
        timestamp=time.time(),
        workflow_step='fetch_invoice',
        outcome='HIT',
        latency_ms=400
    ))
    # Event 2: cross-boundary error (fetching wrong user's record)
    logger.log(RetrievalEvent(
        query='fetch settings for user 456',
        intended_boundary='user',
        provenance='doc_999',
        timestamp=time.time(),
        workflow_step='fetch_settings',
        outcome='CROSS-BOUNDARY',
        latency_ms=300
    ))
    # Event 3: retrieval, but high latency
    logger.log(RetrievalEvent(
        query='fetch past order',
        intended_boundary='session',
        provenance='doc_990',
        timestamp=time.time(),
        workflow_step='order_lookup',
        outcome='HIT',
        latency_ms=1500
    ))
    # Event 4: omitted context
    logger.log(RetrievalEvent(
        query='get previous screen',
        intended_boundary='ui',
        provenance='screen_hash_abc',
        timestamp=time.time(),
        workflow_step='screen_parse',
        outcome='OMITTED',
        latency_ms=200
    ))
    score, total = aggregate_score(logger.events)
    print(f"Score: {score:.2f}/{total}")
    print(f"Boundary Errors: {summarize_boundary_errors(logger.events)}")
    print(f"Latency Breaches: {summarize_latency_breaches(logger.events)}")
    for ev in logger.events:
        print(ev)

if __name__ == "__main__":
    simulate_agent_workflow()