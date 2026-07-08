from typing import Optional, List, Dict, Any
from dataclasses import dataclass, field

@dataclass
class AuditCard:
    step: int
    claim: str
    evidence: Optional[str]
    evidence_type: str  # observation/inference/preference/instruction/permission/outcome
    memory_read: Optional[str]
    permission: Optional[str]
    action: str
    expected_outcome: str
    observed_outcome: Optional[str]
    boundary_failures: List[str] = field(default_factory=list)

    def check_boundaries(self):
        failures = []
        if not self.evidence:
            failures.append("missing_evidence")
        if self.evidence_type not in (
            "observation", "inference", "preference", "instruction", "permission", "outcome"):
            failures.append("unknown_evidence_type")
        if not self.permission:
            failures.append("permission_gap")
        if self.expected_outcome and self.observed_outcome:
            if self.expected_outcome != self.observed_outcome:
                failures.append("unverifiable_outcome")
        if self.memory_read and "other_user" in self.memory_read:
            failures.append("over_broad_memory_use")
        self.boundary_failures = failures
        return failures

def score_audit_trace(trace: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    cards = [AuditCard(**step) for step in trace]
    report = []
    for card in cards:
        failures = card.check_boundaries()
        report.append({
            "step": card.step,
            "claim": card.claim,
            "failures": failures
        })
    return report

if __name__ == "__main__":
    # Simple CLI for demo purposes
    import sys, json
    with open(sys.argv[1]) as f:
        trace = json.load(f)
    results = score_audit_trace(trace)
    print(json.dumps(results, indent=2))