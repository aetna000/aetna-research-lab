import json
import sys
from schema import EvidenceStep, EvidenceChainEpisode


def load_episode(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    steps = []
    for step in data['steps']:
        steps.append(EvidenceStep(
            screen_image_path=step.get('screen_image'),
            ui_structure=step.get('ui_structure'),
            inferred_intent=step.get('inferred_intent'),
            action=step.get('action'),
            rationale=step.get('rationale'),
            outcome_label=step.get('outcome_label'),
            next_screen_image_path=step.get('next_screen_image')
        ))
    return EvidenceChainEpisode(steps)

def replay_episode(episode):
    for i, step in enumerate(episode.steps):
        print(f"=== Step {i+1} ===")
        print(f"Screen: {step.screen_image_path}")
        print(f"UI Structure: {step.ui_structure}")
        print(f"Inferred Intent: {step.inferred_intent}")
        print(f"Action: {step.action}")
        print(f"Rationale: {step.rationale}")
        print(f"Outcome Label: {step.outcome_label}")
        print(f"Next Screen: {step.next_screen_image_path}")
        input("Press Enter for next step...")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python replay.py [episode_file.json]")
        sys.exit(1)
    episode = load_episode(sys.argv[1])
    replay_episode(episode)