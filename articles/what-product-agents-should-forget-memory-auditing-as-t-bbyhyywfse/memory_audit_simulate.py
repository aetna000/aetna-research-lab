import datetime
from memory_audit import UIState, MemoryEntry, AgentAction, MemoryAuditLog

def demo():
    log = MemoryAuditLog()
    # Step 1: open login screen
    ui1 = UIState('login.png', {'fields': ['username', 'password'], 'btn': 'login'}, datetime.datetime.now().isoformat())
    mem1 = MemoryEntry('user: alice', ui1.id, datetime.datetime.now().isoformat())
    log.log_step(ui1, [mem1], [], AgentAction('fill_form', {'fields': {'username':'alice'}}, [mem1.id], 'Fills username'))

    # Step 2: login succeeds, new UI, remember session token
    ui2 = UIState('dashboard.png', {'widgets': ['stats', 'log out']}, datetime.datetime.now().isoformat())
    mem2 = MemoryEntry('session_token:abc', ui2.id, datetime.datetime.now().isoformat())
    log.log_step(ui2, [mem2], [], AgentAction('navigate', {'to': 'stats'}, [mem2.id], 'Uses session token'))

    # Step 3: privacy boundary, forget session token
    ui3 = UIState('logout.png', {'info': 'logged out'}, datetime.datetime.now().isoformat())
    mem2r = MemoryEntry('session_token:abc', ui2.id, datetime.datetime.now().isoformat(), rationale='explicit user logout, privacy')
    log.log_step(ui3, [], [mem2r], AgentAction('noop', {}, [], 'User logged out, cleared memory'))

    log.save('fixture_workflow.json')
    print('Simulation log created: fixture_workflow.json')

if __name__ == '__main__':
    demo()