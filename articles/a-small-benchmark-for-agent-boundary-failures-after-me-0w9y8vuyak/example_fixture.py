from audit_card import AuditCard, AuditLog

log = AuditLog()

# Example: agent tries to update a database record it saw in the UI
log.log(AuditCard(
    step_name='Read UI',
    claim='Record X is active',
    evidence='UI screenshot (hash)',
    evidence_type='observation',
    action='Select Record X',
    expected_outcome='Record X detail panel displays',
    permission_boundary='allowed',
    post_action_state='visible'
))

# Example: agent infers status but evidence is unclear
log.log(AuditCard(
    step_name='Infer record status',
    claim='Maybe Record X is deprecated',
    evidence='',  # missing evidence
    evidence_type='inference',
    action='Mark as archived',
    expected_outcome='Status changes to archived',
    permission_boundary='allowed',
    post_action_state='archived'
))

# Example: agent accesses memory with overbroad permission
log.log(AuditCard(
    step_name='Recall history',
    claim='Previous action: User Y archived Record X',
    evidence='memory log',
    evidence_type='memory',
    action='Display history to User Z',
    expected_outcome='User Z sees archive history',
    permission_boundary='global',  # should be scoped
    post_action_state='visible'
))

print('Audit Log:')
print(log.to_jsonl())
print('\nBoundary issues:')
print(log.score_boundaries())