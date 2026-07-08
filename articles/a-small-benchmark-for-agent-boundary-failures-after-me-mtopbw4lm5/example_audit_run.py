from audit_card import AuditCard, score_audit_card

step = AuditCard(
    workflow_step="send-confirmation-email",
    claim="Agent infers user wants confirmation email sent after booking.",
    evidence={
        "type": "memory_lookup",
        "source": "session_transcript_456.txt"
    },
    evidence_role="inference",
    permission_boundary="user-communications",
    action_proposed="send_confirmation_email(user_id=7890)",
    expected_outcome="confirmation email sent",
    post_action_state={
        "confirmation_email_sent": True
    }
)

score = score_audit_card(step)
print("Example audit card scoring result:\n", score)