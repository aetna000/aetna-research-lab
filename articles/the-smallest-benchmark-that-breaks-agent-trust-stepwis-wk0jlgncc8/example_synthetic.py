from evidence_chain import EvidenceChain

# Step 0: Agent sees a login screen
pre_screen0 = "login_screen_v1.png"  # (placeholder)
ui_map0 = {"fields": ["username", "password"], "buttons": ["Login", "Help"]}
intent0 = "Enter username/password to log in."
evidence_refs0 = ["field:username", "field:password", "button:Login"]
action0 = "Input creds, click Login"
rationale0 = "Both fields are empty, user wants to access main app. 'Login' button is enabled."
post_screen0 = "main_screen_v1.png"
outcome_diff0 = "Login successful, main UI loaded"
attribution0 = "test_agent"
failure0 = None

# Step 1: Agent lands on main screen, sees 'Compose Email' button
pre_screen1 = "main_screen_v1.png"
ui_map1 = {"buttons": ["Compose Email", "Inbox", "Logout"]}
intent1 = "Open compose window to draft a new email."
evidence_refs1 = ["button:Compose Email"]
action1 = "Click 'Compose Email'"
rationale1 = "'Compose Email' button is visible and enabled, next required workflow step."
post_screen1 = "compose_window_v1.png"
outcome_diff1 = "Compose window opened"
attribution1 = "test_agent"
failure1 = None

ec = EvidenceChain()
ec.add_step(pre_screen=pre_screen0, ui_map=ui_map0, intent=intent0, evidence_refs=evidence_refs0, action=action0, rationale=rationale0, post_screen=post_screen0, outcome_diff=outcome_diff0, attribution=attribution0, failure=failure0)
ec.add_step(pre_screen=pre_screen1, ui_map=ui_map1, intent=intent1, evidence_refs=evidence_refs1, action=action1, rationale=rationale1, post_screen=post_screen1, outcome_diff=outcome_diff1, attribution=attribution1, failure=failure1)

print("\n--- Evidence Chain Replay ---")
ec.replay()

print("\n--- Evidence Chain Log as JSON ---")
print(ec.to_json())