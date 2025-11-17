from src.game_theory.games.stochastic_game import StochasticGame
import numpy as np

print("--- Stochastic Game Example ---")

# Define the components of a simple 2-state, 2-player stochastic game
states = ["S1", "S2"]
actions_p1 = ["A1", "A2"]
actions_p2 = ["B1", "B2"]

# Transitions: (current_state, action_p1, action_p2) -> {next_state: probability}
transitions = {
    ("S1", "A1", "B1"): {"S1": 0.8, "S2": 0.2},
    ("S1", "A1", "B2"): {"S1": 0.3, "S2": 0.7},
    ("S1", "A2", "B1"): {"S1": 0.6, "S2": 0.4},
    ("S1", "A2", "B2"): {"S1": 0.1, "S2": 0.9},

    ("S2", "A1", "B1"): {"S1": 0.1, "S2": 0.9},
    ("S2", "A1", "B2"): {"S1": 0.7, "S2": 0.3},
    ("S2", "A2", "B1"): {"S1": 0.4, "S2": 0.6},
    ("S2", "A2", "B2"): {"S1": 0.9, "S2": 0.1},
}

# Rewards: (current_state, action_p1, action_p2) -> (reward_p1, reward_p2)
rewards = {
    ("S1", "A1", "B1"): (1, 1),
    ("S1", "A1", "B2"): (0, 2),
    ("S1", "A2", "B1"): (2, 0),
    ("S1", "A2", "B2"): (-1, -1),

    ("S2", "A1", "B1"): (2, 2),
    ("S2", "A1", "B2"): (1, 0),
    ("S2", "A2", "B1"): (0, 1),
    ("S2", "A2", "B2"): (-2, -2),
}

# Create the stochastic game instance
game = StochasticGame(
    name="Simple 2-State Game",
    states=states,
    actions_p1=actions_p1,
    actions_p2=actions_p2,
    transitions=transitions,
    rewards=rewards
)

# Play the game for a few episodes
# For simplicity, agents will choose random actions in this demo
result = game.play_game(agent1=None, agent2=None, episodes=5, steps_per_episode=5)

print("\n--- End of Stochastic Game Example ---")
