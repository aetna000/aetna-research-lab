'''Minimal schema for a single ARRB test episode.'''

ARRB_EPISODE_SCHEMA = {
    'step_id': str,  # unique identifier
    'workflow_id': str,  # workflow or scenario reference
    'injected_memory': [  # list of dicts for memory injected/available
        {
            'item_id': str,
            'type': str,  # e.g. 'clean', 'revoked', 'ambiguous', 'cross_user', etc.
            'permissible': bool  # should agent be able to recall this?
        }
    ],
    'agent_retrieved': [  # list of str item_ids agent actually used/recalled
        str
    ],
    'ground_truth': {
        'should_recall': [str],   # ids permissible to recall
        'should_not_recall': [str]  # forbidden recall ids
    },
    'annotations': {
        'false_recalls': [str],    # agent retrieved forbidden ids
        'recall_misses': [str],    # agent missed needed ids
        'mixed_confusion': bool,   # ambiguous/unclear retrieval
        'notes': str
    }
}