import json
from rba_schema import RetrievalEvent
from typing import List

def log_event(event: RetrievalEvent, filename: str):
    with open(filename, "a") as f:
        f.write(event.to_json() + "\n")

def load_trace(filename: str) -> List[RetrievalEvent]:
    events = []
    with open(filename) as f:
        for line in f:
            d = json.loads(line)
            events.append(RetrievalEvent(**d))
    return events