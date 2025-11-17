from src.game_theory.games.bargaining_game import BargainingGame

# Define simple linear utility functions
def u1(x):
    return x
def u2(x):
    return x

print("\n--- Bargaining Game Example (Nash Bargaining Solution) ---")
game = BargainingGame(player1_utility_function=u1, player2_utility_function=u2, disagreement_point=(0.1, 0.1))
solution = game.solve_nash_bargaining_solution()
for key, value in solution.items():
    print(f"  {key}: {value}")