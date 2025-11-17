from src.game_theory.games.coalition_formation import CoalitionFormationGame

# Define a characteristic function for a 2-player game
# v({1}) = 1, v({2}) = 1, v({1,2}) = 3
def simple_char_function(coalition):
    if coalition == frozenset([1]):
        return 1
    elif coalition == frozenset([2]):
        return 1
    elif coalition == frozenset([1, 2]):
        return 3
    return 0 # For empty or other unexpected coalitions

print("\n--- Coalition Formation Game Example (Finding the Core) ---")
players = [1, 2]
game = CoalitionFormationGame(players, simple_char_function)
core_result = game.find_core()
print(f"Players: {game.players}")
print(f"Core Result: {core_result}")

# Example for 3 players (simplified output)
players_3 = [1, 2, 3]
def char_function_3_players(coalition):
    if coalition == frozenset([1, 2, 3]):
        return 10
    elif len(coalition) == 1:
        return 1
    elif len(coalition) == 2:
        return 4
    return 0

game_3 = CoalitionFormationGame(players_3, char_function_3_players)
core_result_3 = game_3.find_core()
print(f"\nPlayers: {game_3.players}")
print(f"Core Result (3 players): {core_result_3}")