from fap_harness import BasicAgentMemory, ForgettingAuditProtocol

if __name__ == "__main__":
    agent = BasicAgentMemory()
    fap = ForgettingAuditProtocol(agent)

    # Step 1: Store sensitive (to-be-forgotten) data
    agent.store("secret_user_token", "XYZ123")
    print("Initial retrieval:", agent.retrieve("secret_user_token"))

    # Step 2: Define a forgetting event (e.g., session ends)
    fap.add_forgetting_event("session_end", ["secret_user_token"])

    # Step 3: Register probe to check if agent still remembers
    fap.add_probe("secret_user_token", "direct")

    # Step 4: Execute forgetting audit
    logs = fap.execute()
    for log in logs:
        print("Audit log:", log)