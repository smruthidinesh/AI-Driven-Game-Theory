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

from src.game_theory.games.bayesian_game import BayesianGame

def test_bayesian_game():
    # Define a simple 2x2 entry game for testing the BayesianGame solver
    players = ["Entrant", "Incumbent"]
    types = {"Incumbent": ["Strong", "Weak"]}
    strategies = {"Entrant": ["Enter", "Stay Out"], "Incumbent": ["Fight", "Accommodate"]}

    # Payoffs (simplified to match the solver's assumptions)
    # Format: (player, player_type, player_action, opponent_action, opponent_type) -> payoff
    payoffs = {
        ("Entrant", None, "Enter", "Fight", "Strong"): -1,
        ("Entrant", None, "Enter", "Accommodate", "Weak"): 1,
        ("Entrant", None, "Stay Out", "Fight", "Strong"): 0,
        ("Entrant", None, "Stay Out", "Accommodate", "Weak"): 0,

        ("Incumbent", "Strong", "Fight", "Enter", None): 1,
        ("Incumbent", "Strong", "Accommodate", "Enter", None): -1,
        ("Incumbent", "Strong", "Fight", "Stay Out", None): 0,
        ("Incumbent", "Strong", "Accommodate", "Stay Out", None): 0,

        ("Incumbent", "Weak", "Fight", "Enter", None): -1,
        ("Incumbent", "Weak", "Accommodate", "Enter", None): 2,
        ("Incumbent", "Weak", "Fight", "Stay Out", None): 0,
        ("Incumbent", "Weak", "Accommodate", "Stay Out", None): 0,
    }

    game = BayesianGame("Test Bayesian Game", players, types, strategies, payoffs)
    solution = game.solve()
    
    expected_solution = {
        "Entrant Strategy": "Stay Out",
        "Incumbent Strategy (if Strong)": "Fight",
        "Incumbent Strategy (if Weak)": "Accommodate"
    }
    assert solution == expected_solution
