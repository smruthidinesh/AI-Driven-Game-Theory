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

from src.game_theory.games.sequential_game import SequentialGame

def test_sequential_game():
    game = SequentialGame("Test Sequential Game")
    solution = game.solve()
    expected_solution = {
        "equilibrium_strategy": "Player 1 takes at the first opportunity",
        "payoffs": (1, 0)
    }
    assert solution == expected_solution
