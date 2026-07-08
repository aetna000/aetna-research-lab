import json
import time
from typing import Dict, Optional

class RBSTLogger:
    def __init__(self, log_path: str = "rbst_log.jsonl"):
        self.log_path = log_path
        self.f = open(self.log_path, 'a')
    
    def log_retrieval(self, *, step_id: int, query: str, intended_boundary: str, provenance: str,
                      outcome: str, ground_truth_boundary: Optional[str] = None, latency_ms: Optional[int] = None):
        event = {
            "step_id": step_id,
            "query": query,
            "intended_boundary": intended_boundary,
            "provenance": provenance,
            "timestamp": time.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
            "latency_ms": latency_ms,
            "outcome": outcome,
        }
        if ground_truth_boundary is not None:
            event["ground_truth_boundary"] = ground_truth_boundary
        self.f.write(json.dumps(event) + "\n")
        self.f.flush()
    
    def close(self):
        self.f.close()

# Example usage fixture:
if __name__ == "__main__":
    logger = RBSTLogger(log_path="demo_rbst_log.jsonl")
    logger.log_retrieval(
        step_id=1, query="Recall invoice for session-12", intended_boundary="user-6-session-12",
        provenance="invoice-db/8372.pdf/page-1", outcome="HIT", latency_ms=85
    )
    logger.log_retrieval(
        step_id=2, query="Get previous chat message", intended_boundary="user-6-session-14",
        provenance="chat.log/2024-06-08-09.txt", outcome="CROSS", latency_ms=140, ground_truth_boundary="user-5-session-13"
    )
    logger.close()