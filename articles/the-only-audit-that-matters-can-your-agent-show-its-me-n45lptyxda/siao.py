from dataclasses import dataclass, asdict
from typing import Any, Dict, List, Optional
import json

@dataclass
class Screen:
    elements: List[Dict[str, Any]]  # e.g. [{'id': 'submit', 'type': 'button', 'text': 'Submit'}]
    raw_image: Optional[str] = None  # Path or placeholder for screenshot

@dataclass
class Intent:
    type: str
    cited_elements: List[str]
    confidence: float
    notes: Optional[str] = None

@dataclass
class Action:
    type: str  # e.g. 'click', 'type', etc.
    element_id: str
    params: Optional[Dict[str, Any]] = None
    evidence: Optional[str] = None

@dataclass
class Outcome:
    ui_change: str  # e.g. description of what changed
    result_state: Dict[str, Any]
    error: Optional[str] = None

@dataclass
class Memory:
    state: Dict[str, Any]  # Any persistent agent state

@dataclass
class StepTrace:
    screen: Screen
    intent: Intent
    action: Action
    outcome: Outcome
    memory: Memory

    def to_json(self):
        return json.dumps({
            'screen': asdict(self.screen),
            'intent': asdict(self.intent),
            'action': asdict(self.action),
            'outcome': asdict(self.outcome),
            'memory': asdict(self.memory)
        }, indent=2)