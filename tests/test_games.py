import sys
import os
import pytest

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

print(f"Project Root added to sys.path: {project_root}")
print(f"Current sys.path: {sys.path}")

try:
    import src
    print("Successfully imported 'src' as a top-level package.")
except ImportError as e:
    print(f"Failed to import 'src' as a top-level package: {e}")

from src.game_theory.games import PrisonerDilemma
from src.multi_agent.agent import GameAgent

def test_prisoner_dilemma():
    game = PrisonerDilemma()
    agent1 = GameAgent("Agent1", strategy="Cooperate")
    agent2 = GameAgent("Agent2", strategy="Defect")
    result = game.play_game(agent1, agent2, rounds=100)
    assert isinstance(result, dict)
    assert "average_payoff1" in result
    assert "average_payoff2" in result
