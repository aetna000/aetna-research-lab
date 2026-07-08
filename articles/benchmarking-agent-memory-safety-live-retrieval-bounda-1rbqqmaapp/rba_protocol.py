"""
Retrieval Boundary Audit (RBA) Protocol – reference implementation.

Defines the core data structures and scoring logic to audit agent memory
retrievals across real workflow steps.
"""

from dataclasses import dataclass, field
from typing import List, Optional
import json
import statistics


# Possible retrieval outcomes
class Outcome:
    HIT = "HIT"
    MISS = "MISS"
    CROSS_BOUNDARY = "CROSS_BOUNDARY"
    OMISSION = "OMISSION"
    ERROR = "ERROR"


@dataclass
class RetrievalEvent:
    query: str                     # retrieval query or trigger
    intended_boundary: str         # user, session, screen_ui, tool
    provenance: str                # source reference (file, hash, IDs)
    outcome: str                   # one of Outcome constants
    latency_ms: float              # retrieval time in ms
    workflow_step_id: str
    timestamp: str


class RBAScorer:
    """
    Scores a set of retrieval events according to the RBA protocol.
    Metrics:
      - boundary_error_rate: fraction of events that are CROSS_BOUNDARY
      - provenance_coverage: fraction of events with non-empty provenance
      - median_latency_ms
      - p95_latency_ms
      - omission_rate: fraction of events that are OMISSION
    """
    def __init__(self, events: List[RetrievalEvent]):
        self.events = events
        self.total = len(events)

    def compute_metrics(self) -> dict:
        if self.total == 0:
            return {}

        boundary_errors = sum(1 for e in self.events if e.outcome == Outcome.CROSS_BOUNDARY)
        omissions = sum(1 for e in self.events if e.outcome == Outcome.OMISSION)
        provenance_tagged = sum(1 for e in self.events if e.provenance)
        latencies = [e.latency_ms for e in self.events]

        metrics = {
            "total_events": self.total,
            "boundary_error_rate": boundary_errors / self.total,
            "provenance_coverage": provenance_tagged / self.total,
            "median_latency_ms": statistics.median(latencies),
            "p95_latency_ms": self._percentile(latencies, 95),
            "omission_rate": omissions / self.total,
        }
        return metrics

    @staticmethod
    def _percentile(data: List[float], percentile: float) -> float:
        size = len(data)
        if size == 0:
            return 0.0
        sorted_data = sorted(data)
        index = (percentile / 100.0) * (size - 1)
        lower = int(index)
        upper = lower + 1 if lower < size - 1 else lower
        weight = index - lower
        return sorted_data[lower] * (1 - weight) + sorted_data[upper] * weight

    def report(self) -> str:
        metrics = self.compute_metrics()
        lines = [
            "Retrieval Boundary Audit (RBA) Report",
            "======================================",
            f"Total events: {metrics.get('total_events', 0)}",
            f"Boundary error rate: {metrics.get('boundary_error_rate', 0):.2%}",
            f"Provenance coverage: {metrics.get('provenance_coverage', 0):.2%}",
            f"Median retrieval latency: {metrics.get('median_latency_ms', 0):.1f} ms",
            f"P95 latency: {metrics.get('p95_latency_ms', 0):.1f} ms",
            f"Omission rate: {metrics.get('omission_rate', 0):.2%}",
        ]
        return "\n".join(lines)


def load_events_from_file(path: str) -> List[RetrievalEvent]:
    with open(path, "r") as f:
        data = json.load(f)
    events = []
    for item in data:
        events.append(RetrievalEvent(
            query=item["query"],
            intended_boundary=item["intended_boundary"],
            provenance=item.get("provenance", ""),
            outcome=item["outcome"],
            latency_ms=item["latency_ms"],
            workflow_step_id=item["workflow_step_id"],
            timestamp=item["timestamp"],
        ))
    return events