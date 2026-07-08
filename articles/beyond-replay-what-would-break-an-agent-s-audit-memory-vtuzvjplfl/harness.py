import json
from agent_stub import AgentStub

class MBAH:
    def __init__(self, agent, workflow_path):
        with open(workflow_path, 'r') as f:
            self.workflow = json.load(f)
        self.agent = agent
        self.trace = []

    def run(self):
        for step_num, step in enumerate(self.workflow['steps']):
            print(f"\n=== Step {step_num+1}: {step['desc']} ===")
            # Present current state to agent
            agent_input = step['state']
            retained, forgotten, min_context = self.agent.inspect_memory(agent_input)
            print("Retained:", retained)
            print("Forgotten/Should be Forgotten:", forgotten)
            # Apply adversarial changes if present
            if 'adversarial' in step:
                print("[Adversarial Injection]", step['adversarial']['desc'])
                self.agent.apply_adversarial(step['adversarial'])
                retained_after, forgotten_after, _ = self.agent.inspect_memory(agent_input)
            else:
                retained_after, forgotten_after = retained, forgotten
            # Audit
            audit_result = self._audit(step, retained_after, forgotten_after)
            # Log trace
            self.trace.append({
                'step': step_num+1,
                'desc': step['desc'],
                'adversarial': step.get('adversarial'),
                'retained': retained_after,
                'forgotten': forgotten_after,
                'audit': audit_result
            })
            print("Audit: ", audit_result)
        # Output final minimal replay trace
        with open('output_audit_trace.json', 'w') as fout:
            json.dump(self.trace, fout, indent=2)
        print("\n== Audit complete. See output_audit_trace.json for the replayable log ==")

    def _audit(self, step, retained, forgotten):
        boundary = step.get('expected_memory', {})
        # For demo: flag if forbidden memory is present, or required memory missing
        errors = []
        for f in boundary.get('forbidden', []):
            if f in retained:
                errors.append(f"Memory boundary failure: forbidden context '{f}' retained")
        for req in boundary.get('required', []):
            if req not in retained:
                errors.append(f"Recall integrity failure: required context '{req}' missing")
        return errors if errors else "PASS"

if __name__ == "__main__":
    import sys
    agent = AgentStub()
    workflow_path = sys.argv[1] if len(sys.argv) > 1 else 'fixtures/ui_workflow_example.json'
    harness = MBAH(agent, workflow_path)
    harness.run()