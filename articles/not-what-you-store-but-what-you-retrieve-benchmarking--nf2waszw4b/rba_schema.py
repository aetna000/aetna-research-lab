import json
from dataclasses import dataclass, asdict, field
from typing import Optional

def strip(s):
    if s is not None: return s.strip()
    return None

@dataclass
class RetrievalBoundaryEvent:
    timestamp: str
    step_id: str
    query: str
    declared_boundary: str
    provenance: str
    user_hash: str
    session_hash: str
    latency_ms: int
    outcome: str  # HIT, MISS, CROSS, AMBIG
    notes: Optional[str] = field(default=None)
    
    def validate(self):
        assert self.timestamp, 'timestamp required'
        assert self.step_id, 'step_id required'
        assert self.query, 'query required'
        assert self.declared_boundary, 'declared_boundary required'
        assert self.provenance, 'provenance required'
        assert self.outcome in ('HIT', 'MISS', 'CROSS', 'AMBIG'), f'Invalid outcome: {self.outcome}'
        assert isinstance(self.latency_ms, int) and self.latency_ms >= 0

    @staticmethod
    def from_jsonline(line):
        d = json.loads(line)
        return RetrievalBoundaryEvent(**d)