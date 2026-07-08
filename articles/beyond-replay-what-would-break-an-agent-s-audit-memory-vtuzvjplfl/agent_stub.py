class AgentStub:
    def __init__(self):
        self.memory = set()
        self.session = 'user1'

    def inspect_memory(self, state):
        # For this stub, treat 'active_context' as what should be remembered
        retained = set(state.get('active_context', [])) | self.memory
        # Simulated privacy policy: auto-wipe anything in state['should_forget']
        forgotten = state.get('should_forget', [])
        for f in forgotten:
            retained.discard(f)
        self.memory = set(retained)
        min_context = state.get('minimal_required', [])
        return list(self.memory), forgotten, min_context

    def apply_adversarial(self, adversarial):
        if adversarial.get('type') == 'session_switch':
            self.session = adversarial.get('target_session', 'user2')
            # On session switch, memory is wiped
            self.memory.clear()
        elif adversarial.get('type') == 'permission_downgrade':
            # On permission loss, wipe specified contexts
            for f in adversarial.get('wipe', []):
                self.memory.discard(f)
        elif adversarial.get('type') == 'data_wipe':
            self.memory -= set(adversarial.get('wipe', []))