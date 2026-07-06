import json
from typing import Dict, Any

def log_event(log_path: str, event: Dict[str, Any]):
    with open(log_path, 'a') as f:
        f.write(json.dumps(event) + '\n')

def simulate_agent_step(pre_screen: Dict[str, Any]) -> Dict[str, Any]:
    # Dummy agent: parse visible elements and select an action citing evidence
    intent = "Edit Profile"
    cited_evidence = pre_screen['ui_elements'][1]  # e.g., 'Edit' button
    action = {
        "type": "click",
        "target_element": cited_evidence,
        "evidence": cited_evidence
    }
    output = {
        "inferred_intent": intent,
        "intent_evidence": cited_evidence,
        "selected_action": action,
        "action_evidence": cited_evidence,
        "confidence": 0.98
    }
    return output

def simulate_action(pre_screen, action):
    # Shallow simulation: if click on 'Edit', add 'Edit Form Open' to state
    if action["target_element"] == "Edit":
        post_screen = pre_screen.copy()
        post_screen["ui_elements"].append("Edit Form")
        post_screen["last_action"] = "edit_opened"
        return post_screen
    # No change otherwise
    post_screen = pre_screen.copy()
    post_screen["last_action"] = "no_effect"
    return post_screen

def main():
    with open("example_fixture.json", "r") as f:
        pre_screen = json.load(f)
    event_log_path = "chain_log_example.json"
    open(event_log_path, 'w').close()  # Reset log
    # Step 1: Log screen pre-state
    log_event(event_log_path, {
        "step": 1,
        "type": "pre_action_screen",
        "screen": pre_screen
    })
    # Step 2: Agent infers intent, action, and evidence
    agent_output = simulate_agent_step(pre_screen)
    log_event(event_log_path, {
        "step": 2,
        "type": "agent_decision",
        **agent_output
    })
    # Step 3: Execute action and log post-state
    post_screen = simulate_action(pre_screen, agent_output['selected_action'])
    log_event(event_log_path, {
        "step": 3,
        "type": "post_action_screen",
        "screen": post_screen,
        "outcome_evidence": post_screen["ui_elements"]
    })
    print(f"Evidence chain logged to {event_log_path}")

if __name__ == "__main__":
    main()