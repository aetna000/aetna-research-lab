import json
from datetime import datetime
from rbd_schema import RetrievalEvent, BoundaryEvent, StepLog, WorkflowTrace

# Simulate agent's memory pool
MEMORY = [
    {'item_id': 'A', 'content': 'user1 secret', 'source': 'user-session', 'permission': 'user1'},
    {'item_id': 'B', 'content': 'common doc', 'source': 'common', 'permission': 'public'},
    {'item_id': 'C', 'content': 'user2 financial', 'source': 'user-session', 'permission': 'user2'},
]

def timestamp():
    return datetime.utcnow().isoformat()

def agent_retrieve(memory, allowed_permission):
    retrievals = []
    for item in memory:
        if item['permission'] == allowed_permission or item['permission'] == 'public':
            retrievals.append(RetrievalEvent(
                item_id=item['item_id'], 
                source=item['source'], 
                used=True, 
                omitted=False
            ))
        else:
            retrievals.append(RetrievalEvent(
                item_id=item['item_id'], 
                source=item['source'], 
                used=False, 
                omitted=True, 
                omission_reason=f"excluded by boundary: {allowed_permission}"
            ))
    return retrievals

def simulate_workflow():
    steps = []
    # Step 1: user1 context
    steps.append(StepLog(
        step_id=1,
        timestamp=timestamp(),
        context={"user": "user1", "session": "sess1", "permission": "user1"},
        retrieval_events=agent_retrieve(MEMORY, "user1"),
        boundary_event=None,
        agent_action="took action for user1"
    ))
    # Step 2: User/session boundary event
    steps.append(StepLog(
        step_id=2,
        timestamp=timestamp(),
        context={"user": "user2", "session": "sess2", "permission": "user2"},
        retrieval_events=agent_retrieve(MEMORY, "user2"),
        boundary_event=BoundaryEvent(
            event_type="user_switch",
            details={"from": "user1", "to": "user2"},
            timestamp=timestamp()
        ),
        agent_action="took action for user2: must NOT retrieve user1 memory"
    ))
    return WorkflowTrace(trace_id="demo_trace_001", steps=steps)

if __name__ == "__main__":
    trace = simulate_workflow()
    # Serialize to JSON for inspection
    def dataclass_to_dict(obj):
        if isinstance(obj, list):
            return [dataclass_to_dict(i) for i in obj]
        elif hasattr(obj, '__dict__'):
            out = {}
            for k, v in obj.__dict__.items():
                out[k] = dataclass_to_dict(v)
            return out
        else:
            return obj
    with open("example_trace.json", "w") as f:
        json.dump(dataclass_to_dict(trace), f, indent=2)
    print("RBD example trace written to example_trace.json")