from src.game_theory.games.bayesian_game import BayesianGame
from src.multi_agent.environment import BayesianGameEnvironment
from src.advanced.machine_learning import RLAgent

# 1. Define the Bayesian Game
payers = ["Entrant", "Incumbent"]
types = {
    "Entrant": ["default"],
    "Incumbent": ["strong", "weak"]
}
strategies = {
    "Entrant": ["Enter", "Stay Out"],
    "Incumbent": ["Fight", "Accommodate"]
}
payoffs = {
    ("Enter", "Fight", "strong"): (-1, 1),
    ("Enter", "Accommodate", "strong"): (1, 2),
    ("Stay Out", "Fight", "strong"): (0, 3),
    ("Stay Out", "Accommodate", "strong"): (0, 3),
    ("Enter", "Fight", "weak"): (-1, 0),
    ("Enter", "Accommodate", "weak"): (1, 2),
    ("Stay Out", "Fight", "weak"): (0, 3),
    ("Stay Out", "Accommodate", "weak"): (0, 3),
}
game = BayesianGame("Entry Game", payers, types, strategies, payoffs)

# 2. Create the Environment
env = BayesianGameEnvironment(game)

# 3. Create the RL Agent
# The agent's actions are the strategies of the Entrant
agent = RLAgent("EntrantAgent", actions=strategies["Entrant"])

# 4. Train the Agent
agent.train(env, episodes=1000)

# 5. Print the Learned Q-values
print("\n--- Learned Q-values ---")
for (state, action), value in sorted(agent.q_table.items()):
    print(f"State: {state}, Action: {action}, Q-value: {value:.2f}")

# Determine the learned policy
print("\n--- Learned Policy ---")
for state in types["Incumbent"]:
    action = agent.act(state, epsilon=0) # Choose best action
    print(f"In state '{state}', the agent learns to '{action}'.")