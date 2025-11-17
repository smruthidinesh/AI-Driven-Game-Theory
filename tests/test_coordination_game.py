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

from src.game_theory.games.coordination_game import CoordinationGame
from src.multi_agent.agent import GameAgent

def test_coordination_game_payoffs():
    game = CoordinationGame()
    
    # Test case 1: Both choose A
    agent1 = GameAgent("Agent1", strategy="A")
    agent2 = GameAgent("Agent2", strategy="A")
    result = game.play_game(agent1, agent2, rounds=1)
    assert result["average_payoff1"] == 1
    assert result["average_payoff2"] == 1

    # Test case 2: Both choose B
    agent1 = GameAgent("Agent1", strategy="B")
    agent2 = GameAgent("Agent2", strategy="B")
    result = game.play_game(agent1, agent2, rounds=1)
    assert result["average_payoff1"] == 1
    assert result["average_payoff2"] == 1

    # Test case 3: Mismatched strategies (A, B)
    agent1 = GameAgent("Agent1", strategy="A")
    agent2 = GameAgent("Agent2", strategy="B")
    result = game.play_game(agent1, agent2, rounds=1)
    assert result["average_payoff1"] == 0
    assert result["average_payoff2"] == 0

    # Test case 4: Mismatched strategies (B, A)
    agent1 = GameAgent("Agent1", strategy="B")
    agent2 = GameAgent("Agent2", strategy="A")
    result = game.play_game(agent1, agent2, rounds=1)
    assert result["average_payoff1"] == 0
    assert result["average_payoff2"] == 0
