import sys
import os

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
from src.multi_agent.bounded_rational_agent import BoundedRationalAgent

if __name__ == "__main__":
    # Initialize the game
    game = BattleOfTheSexes()

    # Define possible actions for Battle of the Sexes
    actions = ["Opera", "Football"]

    # Initialize Bounded Rational agents
    # Agent 1 prefers Opera, Agent 2 prefers Football
    agent1 = BoundedRationalAgent(name="BoundedRational 1", actions=actions, strategy="Tit-for-Tat", error_probability=0.1)
    agent2 = BoundedRationalAgent(name="BoundedRational 2", actions=actions, strategy="Tit-for-Tat", error_probability=0.1)

    print("\n--- Bounded Rationality Battle of the Sexes Simulation ---")
    # Run the game for a number of rounds
    results = game.play_game(agent1, agent2, rounds=100)

    print(f"Agent 1 Average Payoff: {results['average_payoff1']:.2f}")
    print(f"Agent 2 Average Payoff: {results['average_payoff2']:.2f}")
