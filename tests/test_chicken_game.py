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

from src.game_theory.games.chicken_game import ChickenGame
from src.multi_agent.agent import GameAgent

def test_chicken_game_payoffs():
    game = ChickenGame()
    
    # Test case 1: Both swerve
    agent1 = GameAgent("Agent1", strategy="Swerve")
    agent2 = GameAgent("Agent2", strategy="Swerve")
    result = game.play_game(agent1, agent2, rounds=1)
    assert result["average_payoff1"] == 0
    assert result["average_payoff2"] == 0

    # Test case 2: Agent 1 swerves, Agent 2 goes straight
    agent1 = GameAgent("Agent1", strategy="Swerve")
    agent2 = GameAgent("Agent2", strategy="Straight")
    result = game.play_game(agent1, agent2, rounds=1)
    assert result["average_payoff1"] == -1
    assert result["average_payoff2"] == 1

    # Test case 3: Agent 1 goes straight, Agent 2 swerves
    agent1 = GameAgent("Agent1", strategy="Straight")
    agent2 = GameAgent("Agent2", strategy="Swerve")
    result = game.play_game(agent1, agent2, rounds=1)
    assert result["average_payoff1"] == 1
    assert result["average_payoff2"] == -1

    # Test case 4: Both go straight
    agent1 = GameAgent("Agent1", strategy="Straight")
    agent2 = GameAgent("Agent2", strategy="Straight")
    result = game.play_game(agent1, agent2, rounds=1)
    assert result["average_payoff1"] == -10
    assert result["average_payoff2"] == -10
