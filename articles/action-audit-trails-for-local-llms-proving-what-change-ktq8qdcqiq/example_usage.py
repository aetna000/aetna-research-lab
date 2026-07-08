"""
Example: creating audit cards for a simulated local LLM agent step.
"""

from audit_card import AuditCard

# Example: file rename operation
card = AuditCard(
    step_id=1,
    input_evidence="screenshots/step1.png",
    memory_context="User request: rename file.txt to report.txt. File list: ['file.txt', 'notes.txt']",
    permission="user",
    proposed_action="rename file.txt to report.txt",
    risk="low"
)

# Simulate the action and capture state before/after
before_state = {"files": ["file.txt", "notes.txt"]}
after_state = {"files": ["report.txt", "notes.txt"]}
card.record_delta(before_state, after_state)

# Verify outcome
card.verify_outcome(success=True, notes="File renamed correctly, new name found in directory.")

# Print the audit record
print("Audit card for step:")
print(card.to_json())

# Check if auditable
print(f"\nAuditable: {card.is_auditable()}")

# Another example: a permission drift scenario
card2 = AuditCard(
    step_id=2,
    input_evidence="screenshots/step2.png",
    memory_context="User requested delete operation on finance folder",
    permission="user",
    proposed_action="delete finance folder",
    risk="high"
)

# But the actual permission at action time was elevated due to a bug
card2.permission = "admin"  # simulate drift
before = {"permissions": "user", "folders": ["finance", "docs"]}
after = {"permissions": "admin", "folders": ["docs"]}
card2.record_delta(before, after)
card2.verify_outcome(success=True, notes="Folder deleted, but permission mismatch detected.")

print("\nSecond audit card (permission drift):")
print(card2.to_json())
print(f"Auditable: {card2.is_auditable()}")