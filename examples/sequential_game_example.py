from src.game_theory.games.sequential_game import SequentialGame

# Create a sequential game (Centipede Game)
game = SequentialGame("Centipede Game", rounds=4)

# Solve the game to find the subgame perfect equilibrium
equilibrium = game.solve()

print(f"--- Sequential Game Example: {game.name} ---")
print("\nEquilibrium found using backward induction:")
for key, value in equilibrium.items():
    print(f"  {key}: {value}")