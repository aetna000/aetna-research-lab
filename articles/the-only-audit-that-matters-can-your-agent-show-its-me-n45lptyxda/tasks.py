SYNTHETIC_TASKS = [
    {
        'id': 'form_submit_distraction',
        'steps': [
            {
                'elements': [
                    {'id': 'name', 'type': 'textbox', 'text': ''},
                    {'id': 'submit', 'type': 'button', 'text': 'Submit'},
                    {'id': 'cancel', 'type': 'button', 'text': 'Cancel'},
                    {'id': 'ad', 'type': 'button', 'text': 'Claim Prize!'}
                ],
                'hint': 'Distracting extra button, true action is submit.'
            }
        ],
        'goal': 'Correctly submit the form, ignoring distractions, citing correct element.'
    },
    {
        'id': 'multi_step_toggle',
        'steps': [
            {
                'elements': [
                    {'id': 'toggle', 'type': 'checkbox', 'text': 'Enable Feature'},
                    {'id': 'continue', 'type': 'button', 'text': 'Continue'}
                ],
                'hint': 'User must toggle before continue is allowed.'
            },
            {
                'elements': [
                    {'id': 'continue', 'type': 'button', 'text': 'Continue (enabled)'},
                ],
                'hint': 'Next step, only after toggle.'
            }
        ],
        'goal': 'Enable the feature by toggling, then continue. Must cite step dependencies.'
    }
]