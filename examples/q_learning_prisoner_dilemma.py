import sys
import os
import numpy as np

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

from src.game_theory.games.prisoner_dilemma import PrisonerDilemma
from src.multi_agent.q_learning_agent import QLearningAgent

print("--- Q-Learning Agent playing Prisoner's Dilemma ---")

# Define actions for the Prisoner's Dilemma
actions = ["Cooperate", "Defect"]

# Create two Q-Learning Agents
agent1 = QLearningAgent("Agent1", actions=actions, epsilon=0.1, learning_rate=0.1, discount_factor=0.9)
agent2 = QLearningAgent("Agent2", actions=actions, epsilon=0.1, learning_rate=0.1, discount_factor=0.9)

game = PrisonerDilemma()

episodes = 1000 # Number of training episodes

# To simplify state representation for Q-learning in a 2-player game:
# State for Agent 1 could be Agent 2's last action.
# State for Agent 2 could be Agent 1's last action.
# Initial state can be 'None' or 'Start'

last_action_agent1 = None
last_action_agent2 = None

for episode in range(episodes):
    # Initial state for the episode (based on previous actions, or a neutral start)
    state1 = last_action_agent2 # Agent 1's state is Agent 2's last action
    state2 = last_action_agent1 # Agent 2's state is Agent 1's last action

    # Agents choose actions
    action1 = agent1.choose_action(state1)
    action2 = agent2.choose_action(state2)

    # Play a round of the game
    payoff1, payoff2 = game.play_round(action1, action2)

    # Agents learn from the outcome
    # The reward for an agent is its payoff
    agent1.learn(action2, payoff1) # Agent 1's next state is Agent 2's current action
    agent2.learn(action1, payoff2) # Agent 2's next state is Agent 1's current action

    last_action_agent1 = action1
    last_action_agent2 = action2

    if (episode + 1) % 100 == 0:
        print(f"Episode {episode + 1}/{episodes} completed.")

print("\n--- Training Complete ---")
print("\nAgent 1 Q-Table (sample):")
for (state, action), q_value in list(agent1.q_table.items())[:5]: # Print first 5 entries
    print(f"  Q({state}, {action}) = {q_value:.2f}")

print("\nAgent 2 Q-Table (sample):")
for (state, action), q_value in list(agent2.q_table.items())[:5]: # Print first 5 entries
    print(f"  Q({state}, {action}) = {q_value:.2f}")

# Evaluate final strategies (simplified: check most chosen action in last state)
# This is a very basic evaluation. A proper evaluation would involve playing without exploration.

# To get a sense of the learned strategy, we can set epsilon to 0 and see what actions are chosen
agent1.epsilon = 0
agent2.epsilon = 0

print("\n--- Final Strategy Evaluation (Epsilon=0) ---")
final_payoff1 = 0
final_payoff2 = 0
num_eval_rounds = 100

for _ in range(num_eval_rounds):
    state1 = last_action_agent2
    state2 = last_action_agent1

    action1 = agent1.choose_action(state1)
    action2 = agent2.choose_action(state2)

    p1, p2 = game.play_round(action1, action2)
    final_payoff1 += p1
    final_payoff2 += p2

    last_action_agent1 = action1
    last_action_agent2 = action2

print(f"Average Payoff Agent 1 (eval): {final_payoff1 / num_eval_rounds:.2f}")
print(f"Average Payoff Agent 2 (eval): {final_payoff2 / num_eval_rounds:.2f}")
