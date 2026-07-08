from worba_harness import run_synthetic_worba_audit

if __name__ == "__main__":
    run = run_synthetic_worba_audit()
    print("--- WORBA Audit Run Result ---")
    print("Trustworthy:", run.trustworthy)
    for step in run.audit_steps:
        print(f"Step {step.step_num}")
        print(f"  Audit Score: {step.audit_score}")
        print(f"  Anomaly Flags: {step.anomaly_flags}")
        for event in step.retrieval_events:
            print(f"    Query: {event.query}")
            print(f"      Scope: {event.query_scope}")
            print(f"      Retrieved: {event.retrieved_memory}")
            print(f"      Boundary Match: {event.boundary_match}")
            print(f"      Leak Detected: {event.leak_detected}")
            print(f"      Ambiguous Provenance: {event.ambiguous_provenance}")
            print(f"      Latency (ms): {event.latency_ms}")