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

from src.game_theory.games.battle_of_the_sexes import BattleOfTheSexes
from src.multi_agent.agent import GameAgent

def test_battle_of_the_sexes_payoffs():
    game = BattleOfTheSexes()
    
    # Test case 1: Both choose Opera
    agent1 = GameAgent("Agent1", strategy="Opera")
    agent2 = GameAgent("Agent2", strategy="Opera")
    result = game.play_game(agent1, agent2, rounds=1)
    assert result["average_payoff1"] == 3
    assert result["average_payoff2"] == 2

    # Test case 2: Both choose Football
    agent1 = GameAgent("Agent1", strategy="Football")
    agent2 = GameAgent("Agent2", strategy="Football")
    result = game.play_game(agent1, agent2, rounds=1)
    assert result["average_payoff1"] == 2
    assert result["average_payoff2"] == 3

    # Test case 3: Mismatched strategies (Opera, Football)
    agent1 = GameAgent("Agent1", strategy="Opera")
    agent2 = GameAgent("Agent2", strategy="Football")
    result = game.play_game(agent1, agent2, rounds=1)
    assert result["average_payoff1"] == 0
    assert result["average_payoff2"] == 0

    # Test case 4: Mismatched strategies (Football, Opera)
    agent1 = GameAgent("Agent1", strategy="Football")
    agent2 = GameAgent("Agent2", strategy="Opera")
    result = game.play_game(agent1, agent2, rounds=1)
    assert result["average_payoff1"] == 0
    assert result["average_payoff2"] == 0
