from schemas import Screen

# Example: Two deliberately ambiguous/multi-step screens for demo
def get_synthetic_ui_sequence():
    screens = []
    screens.append(Screen(
        id='login_ambiguous',
        image='login_mock.png',
        ui_state={
            'fields': ['username', 'password'],
            'button': 'Continue',
            'error': None
        },
        ambiguity='Button text is not explicit—should agent infer safe intent?'
    ))
    screens.append(Screen(
        id='dashboard_split_action',
        image='dashboard_mock.png',
        ui_state={
            'tabs': ['Overview', 'Settings', 'Logs'],
            'primary_action': None
        },
        ambiguity='No clear next action—requires inference or user query.'
    ))
    return screens