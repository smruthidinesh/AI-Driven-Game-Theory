from src.game_theory.games.bayesian_game import BayesianGame

# Define the components of the Bayesian Entry Game
players = ["Entrant", "Incumbent"]

# Types for each player (Incumbent has two types, Entrant has one)
types = {
    "Entrant": ["default"],
    "Incumbent": ["strong", "weak"]
}

# Strategies for each player
strategies = {
    "Entrant": ["Enter", "Stay Out"],
    "Incumbent": ["Fight", "Accommodate"]
}

# Payoffs: (Entrant, Incumbent)
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

# Create a Bayesian game instance
game = BayesianGame("Entry Game", players, types, strategies, payoffs)

# Solve the game
equilibrium = game.solve()

print(f"--- Bayesian Game Example: {game.name} ---")
print("\nEquilibrium found:")
for strategy, action in equilibrium.items():
    print(f"  {strategy}: {action}")