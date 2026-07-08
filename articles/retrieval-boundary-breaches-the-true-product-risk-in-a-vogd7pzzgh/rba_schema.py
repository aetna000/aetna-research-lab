import json

RBA_SCHEMA = [
    "timestamp",           # ISO 8601
    "step_id",             # Workflow step
    "agent_version",       # Agent stack or code version
    "task_desc",           # Human label for step/task
    "retrieval_query",     # NL or structured retrieval query/trigger
    "intended_boundary",   # e.g., user, session, tool, ui_context
    "provenance",          # File, screen hash, session/user ID
    "retrieval_result",    # HIT / MISS / CROSS-BOUNDARY / OMIT / ERROR
    "latency_ms"           # Optional, integer
]

def validate_rba_event(event):
    for field in RBA_SCHEMA:
        if field not in event:
            raise ValueError(f'Missing RBA field: {field}')
    # Basic checks
    if event['retrieval_result'] not in ["HIT","MISS","CROSS-BOUNDARY","OMIT","ERROR"]:
        raise ValueError('Invalid retrieval_result value')
    return True