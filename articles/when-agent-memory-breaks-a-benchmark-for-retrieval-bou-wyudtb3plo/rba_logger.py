import json
from dataclasses import dataclass, asdict
from typing import Dict, Optional

@dataclass
class RBAEvent:
    query: str  # retrieval NL/structured query
    intent_scope: Dict[str, str]  # e.g., {'user': 'X', 'session': 'S1'}
    provenance: Dict[str, str]    # e.g., {'source': 'file:A', 'ui_hash': 'abc'}
    latency_ms: int
    workflow: Dict[str, str]      # e.g., {'step_id': '3', 'timestamp_iso': '2024-06-20T12:00Z'}
    outcome: str                  # 'HIT','OMISSION','CROSS-BOUNDARY','AMBIGUOUS','ERROR'
    notes: Optional[str] = None

    def to_json(self):
        return json.dumps(asdict(self), ensure_ascii=False)

class RBAEventLogger:
    def __init__(self, outfile):
        self.outfile = outfile
    def log(self, event: RBAEvent):
        with open(self.outfile, 'a', encoding='utf-8') as f:
            f.write(event.to_json()+"\n")