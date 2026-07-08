from audit_logging import RetrievalEvent

def score_event(event: RetrievalEvent, latency_threshold_ms=1000) -> float:
    if event.outcome == 'HIT':
        if event.latency_ms is not None and event.latency_ms > latency_threshold_ms:
            return 0.5  # Penalize for latency breach, partial credit
        return 1.0
    if event.outcome == 'CROSS-BOUNDARY':
        return -1.0
    if event.outcome == 'MISS':
        return 0.0
    if event.outcome == 'OMITTED':
        return 0.0
    return 0.0

def aggregate_score(events, latency_threshold_ms=1000):
    total = 0
    for ev in events:
        total += score_event(ev, latency_threshold_ms=latency_threshold_ms)
    return total, len(events)
    
def summarize_boundary_errors(events):
    err = [ev for ev in events if ev.outcome == 'CROSS-BOUNDARY']
    return len(err)

def summarize_latency_breaches(events, latency_threshold_ms=1000):
    lat = [ev for ev in events if ev.latency_ms and ev.latency_ms > latency_threshold_ms]
    return len(lat)