import sys
import os

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from src.game_theory.games.prisoner_dilemma import PrisonerDilemma
from src.multi_agent.environment import PrisonerDilemmaEnvironment
from src.advanced.machine_learning import RLAgent

# 1. Define the Game
game = PrisonerDilemma()

# 2. Create the Environment
env = PrisonerDilemmaEnvironment(game)

# 3. Create the RL Agent
# The agent's actions are "Cooperate" or "Defect"
agent = RLAgent("PrisonerAgent", actions=["Cooperate", "Defect"])

# 4. Train the Agent
agent.train(env, episodes=1000)

# 5. Print the Learned Q-values
print("\n--- Learned Q-values ---")
for (state, action), value in sorted(agent.q_table.items()):
    print(f"State: {state}, Action: {action}, Q-value: {value:.2f}")

# Determine the learned policy
print("\n--- Learned Policy ---")
state = "start"
action = agent.act(state, epsilon=0) # Choose best action
print(f"In the 'start' state, the agent learns to '{action}'.")