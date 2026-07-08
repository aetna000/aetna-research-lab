from siao_schema import SIAOStep, SIAOChain

# Simulate a toy 3-step agent workflow
chain = SIAOChain()

# Step 1
chain.add(SIAOStep(
    step_id=1,
    pre_screen="screen1.png",
    parsed_ui=[{"type": "button", "label": "Login", "loc": [100,50,150,80]}],
    intent="Find and click the Login button to continue",
    evidence=["button:Login"],
    action="click(Login)",
    rationale="Login is the only actionable element on this screen.",
    post_screen="screen2.png",
    outcome="Login button pressed, navigated to home screen."
))

# Step 2
chain.add(SIAOStep(
    step_id=2,
    pre_screen="screen2.png",
    parsed_ui=[{"type": "input", "label": "Search", "loc": [70,70,300,90]}],
    intent="Input search query in the Search box",
    evidence=["input:Search"],
    action="type('budget report')",
    rationale="User’s workflow requires a budget report; Search box is present.",
    post_screen="screen3.png",
    outcome="Text 'budget report' entered in Search."
))

# Step 3
chain.add(SIAOStep(
    step_id=3,
    pre_screen="screen3.png",
    parsed_ui=[{"type": "button", "label": "Submit", "loc": [120,100,180,130]}],
    intent="Submit the search query.",
    evidence=["button:Submit"],
    action="click(Submit)",
    rationale="Submit is the next logical action with query text present.",
    post_screen="screen4.png",
    outcome="Query submitted; search results displayed."
))

# Output the full chain as JSON
chain.to_json("example_trace.json")