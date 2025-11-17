import sys
import os

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) # Corrected: only one '..'
sys.path.insert(0, project_root)

print(f"Project Root added to sys.path: {project_root}")
print(f"Current sys.path: {sys.path}")

try:
    import src
    print("Successfully imported 'src' as a top-level package.")
except ImportError as e:
    print(f"Failed to import 'src' as a top-level package: {e}")

from src.game_theory.games.prisoner_dilemma import PrisonerDilemma
from src.multi_agent.q_learning_agent import QLearningAgent

if __name__ == "__main__":
    # Initialize the game
    game = PrisonerDilemma()

    # Define possible actions for Q-learning agents
    actions = ["Cooperate", "Defect"]

    # Initialize Q-learning agents
    agent1 = QLearningAgent(name="QLearner 1", actions=actions, learning_rate=0.1, discount_factor=0.9, epsilon=0.1)
    agent2 = QLearningAgent(name="QLearner 2", actions=actions, learning_rate=0.1, discount_factor=0.9, epsilon=0.1)

    print("\n--- Q-Learning Prisoner's Dilemma Simulation ---")
    # Run the game for many rounds to allow agents to learn
    results = game.play_game(agent1, agent2, rounds=1000)

    print(f"Agent 1 Average Payoff: {results['average_payoff1']:.2f}")
    print(f"Agent 2 Average Payoff: {results['average_payoff2']:.2f}")

    # You can inspect the Q-tables to see what the agents learned
    # print("\nAgent 1 Q-Table:", agent1.q_table)
    # print("\nAgent 2 Q-Table:", agent2.q_table)

    # To see learned behavior, you might want to run another game with epsilon=0 (no exploration)
    agent1_eval = QLearningAgent(name="QLearner 1 Eval", actions=actions, learning_rate=0.1, discount_factor=0.9, epsilon=0.0)
    agent2_eval = QLearningAgent(name="QLearner 2 Eval", actions=actions, learning_rate=0.1, discount_factor=0.9, epsilon=0.0)

    # Copy learned Q-tables
    agent1_eval.q_table = agent1.q_table
    agent2_eval.q_table = agent2.q_table

    print("\n--- Q-Learning Prisoner's Dilemma Evaluation (Epsilon=0) ---")
    eval_results = game.play_game(agent1_eval, agent2_eval, rounds=100)
    print(f"Agent 1 Evaluation Average Payoff: {eval_results['average_payoff1']:.2f}")
    print(f"Agent 2 Evaluation Average Payoff: {eval_results['average_payoff2']:.2f}")
