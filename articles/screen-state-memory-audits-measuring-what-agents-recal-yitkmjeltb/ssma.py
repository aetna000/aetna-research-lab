#!/usr/bin/env python3
"""Minimal SSMA protocol simulation."""

class ScreenState:
    def __init__(self, step_id, ui_elements):
        self.step_id = step_id
        self.ui_elements = ui_elements  # dict: element_id -> text/value

class AgentMemoryRetrieval:
    def __init__(self, query, retrieved_context, provenance, omission_log=None):
        self.query = query
        self.retrieved_context = retrieved_context  # list of (fragment, source)
        self.provenance = provenance  # dict with source explanation
        self.omission_log = omission_log or []  # items deliberately omitted

class AuditLog:
    def __init__(self):
        self.steps = []

    def add_step(self, step_id, retrieval, ground_truth_retrieval, ground_truth_omissions):
        true_positive = len(set(retrieval.retrieved_context) & set(ground_truth_retrieval))
        false_positive = len(set(retrieval.retrieved_context) - set(ground_truth_retrieval))
        false_negative = len(set(ground_truth_retrieval) - set(retrieval.retrieved_context))
        precision = true_positive / (true_positive + false_positive) if (true_positive + false_positive) > 0 else 0
        recall = true_positive / (true_positive + false_negative) if (true_positive + false_negative) > 0 else 1
        omission_correct = set(retrieval.omission_log) == set(ground_truth_omissions)
        false_omissions = list(set(ground_truth_omissions) - set(retrieval.omission_log))
        false_retentions = list(set(retrieval.omission_log) - set(ground_truth_omissions))
        self.steps.append({
            "step_id": step_id,
            "retrieval_precision": precision,
            "retrieval_recall": recall,
            "omission_correct": omission_correct,
            "false_omissions": false_omissions,
            "false_retentions": false_retentions,
        })

    def summary(self):
        if not self.steps:
            return {}
        total_precision = sum(s["retrieval_precision"] for s in self.steps) / len(self.steps)
        total_recall = sum(s["retrieval_recall"] for s in self.steps) / len(self.steps)
        omission_accuracy = sum(1 for s in self.steps if s["omission_correct"]) / len(self.steps)
        return {
            "total_steps": len(self.steps),
            "avg_retrieval_precision": total_precision,
            "avg_retrieval_recall": total_recall,
            "omission_accuracy": omission_accuracy,
        }

def simulate_workflow():
    audit = AuditLog()

    # Step 1: Normal screen, agent retrieves correctly
    screen1 = ScreenState(1, {"btn": "Submit", "label": "Order #123"})
    retrieval1 = AgentMemoryRetrieval(
        query="How many items?",
        retrieved_context=["Order #123 details"],
        provenance={"source": "screen"},
        omission_log=["user_address"]
    )
    ground_truth_retrieval1 = ["Order #123 details"]
    ground_truth_omissions1 = ["user_address"]
    audit.add_step(1, retrieval1, ground_truth_retrieval1, ground_truth_omissions1)

    # Step 2: Adversarial UI with overlapping elements, agent incorrectly retrieves cross-session data
    screen2 = ScreenState(2, {"btn": "Submit", "label": "Order #456"})
    retrieval2 = AgentMemoryRetrieval(
        query="Check status",
        retrieved_context=["Order #123 details", "Order #456 details"],
        provenance={"source": "memory"},
        omission_log=[]
    )
    ground_truth_retrieval2 = ["Order #456 details"]  # should only use current screen
    ground_truth_omissions2 = ["Order #123 details"]  # must omit cross-session
    audit.add_step(2, retrieval2, ground_truth_retrieval2, ground_truth_omissions2)

    # Step 3: Agent misses a key UI element entirely
    screen3 = ScreenState(3, {"btn": "Cancel", "warning": "Policy not accepted"})
    retrieval3 = AgentMemoryRetrieval(
        query="Can I cancel?",
        retrieved_context=["Cancel button visible"],
        provenance={"source": "screen"},
        omission_log=["warning"]  # agent claims to have omitted warning
    )
    ground_truth_retrieval3 = ["Cancel button visible", "Warning: Policy not accepted"]
    ground_truth_omissions3 = []  # nothing should be omitted
    audit.add_step(3, retrieval3, ground_truth_retrieval3, ground_truth_omissions3)

    print("SSMA Audit Results:")
    for step in audit.steps:
        print(f"Step {step['step_id']}: P={step['retrieval_precision']:.2f}, R={step['retrieval_recall']:.2f}, OmitOK={step['omission_correct']}")
    print("Summary:", audit.summary())

if __name__ == "__main__":
    simulate_workflow()