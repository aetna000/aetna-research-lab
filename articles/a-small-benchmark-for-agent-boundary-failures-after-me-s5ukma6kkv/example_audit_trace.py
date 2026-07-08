from audit_card import AuditCard, AuditScorer, BoundaryType

def main():
    steps = [
        AuditCard(
            step_id="1",
            workflow_step="Read invoice screen",
            claim="User owes $200",
            boundary_type=BoundaryType.OBSERVATION,
            source_evidence="screenshot_2024-06-18T09:00:00.png",
            memory_state="Invoice view",
        ),
        AuditCard(
            step_id="2",
            workflow_step="Infer payment method",
            claim="Payment account is bank A",
            boundary_type=BoundaryType.INFERENCE,
            source_evidence="parsed_text: account=bank_a",
            memory_state="Prior user payment settings",
        ),
        AuditCard(
            step_id="3",
            workflow_step="Attempt payment",
            claim="Action: Paid $200 via bank A",
            boundary_type=BoundaryType.ACTION,
            source_evidence="UI click: pay_button",
            permission="can_pay",
            action="click_pay",
            expected_outcome="Payment processed",
            post_action_observation=None,  # Did not verify outcome
            boundary_failures=["unverifiable_outcome"],
            notes="No confirmation UI present"
        )
    ]

    scorer = AuditScorer(audit_cards=steps)
    print("Per-boundary failure counts:", scorer.score_boundaries())
    print("Overall workflow success:", scorer.overall_success())

if __name__ == "__main__":
    main()