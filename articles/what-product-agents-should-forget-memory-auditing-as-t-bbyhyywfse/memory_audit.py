import json
import hashlib
from typing import List, Dict, Optional

class UIState:
    def __init__(self, screen: str, ui_parse: dict, timestamp: str):
        self.screen = screen              # e.g., 'screen1.png'
        self.ui_parse = ui_parse          # parsed structure (dict)
        self.timestamp = timestamp        # ISO format
        concat = str(screen) + str(ui_parse) + timestamp
        self.id = hashlib.sha256(concat.encode()).hexdigest()[:12]

class MemoryEntry:
    def __init__(self, content: str, source_ui_id: str, ts: str, rationale: Optional[str]=None):
        self.content = content
        self.source_ui_id = source_ui_id
        self.timestamp = ts
        self.rationale = rationale  # For redacted/removed memories
        self.id = hashlib.sha256((content+source_ui_id+ts).encode()).hexdigest()[:12]

class AgentAction:
    def __init__(self, action_type: str, params: dict, cited_memories: List[str], rationale: str):
        self.action_type = action_type
        self.params = params
        self.cited_memories = cited_memories
        self.rationale = rationale

class MemoryAuditLog:
    def __init__(self):
        self.steps = []  # Each step: {step_idx, ui_state, memories_added, memories_removed, action}

    def log_step(self, ui_state, memories_added, memories_removed, action):
        step = {
            'step_idx': len(self.steps)+1,
            'ui_state_id': ui_state.id,
            'ui_parse': ui_state.ui_parse,
            'screen': ui_state.screen,
            'timestamp': ui_state.timestamp,
            'added_memories': [{
                'id': m.id,
                'content': m.content,
                'source_ui_id': m.source_ui_id,
                'timestamp': m.timestamp
            } for m in memories_added],
            'removed_memories': [{
                'id': m.id,
                'content': m.content,
                'source_ui_id': m.source_ui_id,
                'timestamp': m.timestamp,
                'rationale': m.rationale
            } for m in memories_removed],
            'action': {
                'type': action.action_type,
                'params': action.params,
                'cited_memories': action.cited_memories,
                'rationale': action.rationale
            }
        }
        self.steps.append(step)

    def save(self, fp):
        with open(fp, 'w') as f:
            json.dump(self.steps, f, indent=2)

    def load(self, fp):
        with open(fp, 'r') as f:
            self.steps = json.load(f)

    def replay(self):
        for s in self.steps:
            print(f"Step {s['step_idx']} | UI_State: {s['ui_state_id']}")
            print(f"  UI Parse: {s['ui_parse']}")
            print(f"  Added Memories: {[m['id'] for m in s['added_memories']]}")
            print(f"  Removed Memories: {[m['id'] for m in s['removed_memories']]}")
            print(f"  Action: {s['action']['type']} | Used Memories: {s['action']['cited_memories']} | Rationale: {s['action']['rationale']}")
            print('-'*65)