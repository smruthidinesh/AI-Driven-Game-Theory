print("Script started!") # Add this line

from src.game_theory.games.signaling_game import SignalingGame

print("--- Signaling Game Example ---")
game = SignalingGame()
equilibrium = game.solve()
print(f"Game: {game.name}")
for key, value in equilibrium.items():
    print(f"  {key}: {value}")