from src.game_theory.games.sequential_game import SequentialGame
from src.multi_agent.environment import SequentialGameEnvironment
from src.advanced.machine_learning import RLAgent

# 1. Define the Sequential Game (Centipede Game)
game = SequentialGame("Centipede Game", rounds=4)

# 2. Create the Environment
env = SequentialGameEnvironment(game)

# 3. Create the RL Agent
# The agent's actions are "Take" or "Pass"
agent = RLAgent("CentipedeAgent", actions=["Take", "Pass"])

# 4. Train the Agent
agent.train(env, episodes=1000)

# 5. Print the Learned Q-values
print("\n--- Learned Q-values ---")
for (state, action), value in sorted(agent.q_table.items()):
    print(f"State: {state}, Action: {action}, Q-value: {value:.2f}")

# Determine the learned policy for Player 1 (agent)
print("\n--- Learned Policy for Player 1 ---")
# We need to check the policy for states where Player 1 makes a decision
# In Centipede, Player 1 makes decisions in rounds 1 and 3 (odd rounds)

# Example for round 1, pot 1
state_r1_p1 = (1, 1)
action_r1_p1 = agent.act(state_r1_p1, epsilon=0) # Choose best action
print(f"In state {state_r1_p1} (Round 1, Pot 1), the agent learns to '{action_r1_p1}'.")

# Example for round 3, pot 4 (if game reaches here)
state_r3_p4 = (3, 4)
action_r3_p4 = agent.act(state_r3_p4, epsilon=0) # Choose best action
print(f"In state {state_r3_p4} (Round 3, Pot 4), the agent learns to '{action_r3_p4}'.")