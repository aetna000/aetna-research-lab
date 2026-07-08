import json
import time
from enum import Enum
from typing import Dict, Any

class RetrievalType(str, Enum):
    IN_SESSION = 'in_session'
    CROSS_SESSION = 'cross_session'
    AMBIGUOUS = 'ambiguous'
    DISTRACTOR = 'distractor'

class RetrievalOutcome(str, Enum):
    ALLOW = 'allow'
    BLOCK = 'block'
    TIMEOUT = 'timeout'
    ERROR = 'error'

def policy_check(retrieval: Dict[str, Any]) -> Dict[str, Any]:
    """
    Simulate retrieval policy enforcement logic. Returns outcome and rationale.
    For demonstration, block cross_session, randomly block ambiguous, allow in_session; always block distractor.
    """
    rtype = retrieval['query_type']
    if rtype == RetrievalType.IN_SESSION:
        return {'outcome': RetrievalOutcome.ALLOW, 'rationale': 'Session match, permissions satisfied.'}
    elif rtype == RetrievalType.CROSS_SESSION:
        return {'outcome': RetrievalOutcome.BLOCK, 'rationale': 'Cross-session retrieval blocked by policy.'}
    elif rtype == RetrievalType.AMBIGUOUS:
        # Block half the time for demonstration
        import random
        if random.random() > 0.5:
            return {'outcome': RetrievalOutcome.ALLOW, 'rationale': 'Provenance resolved; permitted on review.'}
        else:
            return {'outcome': RetrievalOutcome.BLOCK, 'rationale': 'Ambiguous provenance/permission: blocked.'}
    else:
        return {'outcome': RetrievalOutcome.BLOCK, 'rationale': 'Distractor: never allowed.'}

def make_event_log(retrieval: Dict[str, Any], outcome_obj: Dict[str, str], latency: float) -> Dict[str, Any]:
    event = {
        'timestamp': time.time(),
        'query': retrieval['query'],
        'query_type': retrieval['query_type'],
        'session_id': retrieval.get('session_id'),
        'provenance': retrieval.get('provenance', {}),
        'policy_context': retrieval.get('policy_context', {}),
        'memory_fragment': retrieval.get('memory_fragment', ''),
        'outcome': outcome_obj['outcome'],
        'rationale': outcome_obj['rationale'],
        'latency_ms': int(latency * 1000)
    }
    return event