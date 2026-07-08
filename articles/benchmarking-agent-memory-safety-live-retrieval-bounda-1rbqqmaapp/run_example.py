"""
Example driver for the Retrieval Boundary Audit (RBA) protocol.
Loads synthetic events from 'example_events.json', computes metrics,
and prints a human-readable report.
"""

from rba_protocol import load_events_from_file, RBAScorer


def main():
    events = load_events_from_file("example_events.json")
    scorer = RBAScorer(events)
    print(scorer.report())


if __name__ == "__main__":
    main()