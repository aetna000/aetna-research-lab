import argparse
import json
from datetime import datetime
from rba_schema import RBA_SCHEMA, validate_rba_event

class RBALogger:
    def __init__(self, filename):
        self.f = open(filename, 'w')
    def log(self, event):
        validate_rba_event(event)
        self.f.write(json.dumps(event) + '\n')
    def close(self):
        self.f.close()

def example():
    logger = RBALogger('example_rba_log.jsonl')
    # Example event: agent queries for user note, stays in boundary
    event1 = {
        'timestamp': datetime.utcnow().isoformat(),
        'step_id': 'step_001',
        'agent_version': 'memgpt-v0.2.5',
        'task_desc': 'Find user project notes',
        'retrieval_query': 'project alpha notes',
        'intended_boundary': 'user:123',
        'provenance': 'doc:456',
        'retrieval_result': 'HIT',
        'latency_ms': 47
    }
    # Example event: agent crosses boundary
    event2 = dict(event1)
    event2.update({
        'step_id': 'step_002',
        'retrieval_query': 'project beta notes',
        'intended_boundary': 'user:123',
        'provenance': 'doc:789',
        'retrieval_result': 'CROSS-BOUNDARY',
        'latency_ms': 51
    })
    # Example event: omission
    event3 = dict(event1)
    event3.update({
        'step_id': 'step_003',
        'retrieval_query': 'team context',
        'intended_boundary': 'user:123',
        'provenance': 'doc:321',
        'retrieval_result': 'OMIT',
        'latency_ms': 10
    })
    for ev in (event1, event2, event3):
        logger.log(ev)
    logger.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='RBA Logger Example')
    parser.add_argument('--logfile', type=str, default='example_rba_log.jsonl')
    args = parser.parse_args()
    example()