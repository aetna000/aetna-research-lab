import sys
from memory_audit import MemoryAuditLog

def main():
    log = MemoryAuditLog()
    log.load('fixture_workflow.json')
    log.replay()

if __name__ == '__main__':
    main()