from src.game_theory.games.game_tree import GameTree, Node

print("--- Game Tree Example: Centipede Game ---")

# Create a GameTree instance
game_tree = GameTree(root_node=None) # Root will be set by build_centipede_game

# Build a Centipede Game tree with 2 rounds
print("Building a 2-round Centipede Game tree...")
game_tree.build_centipede_game(rounds=2)

# Print the tree structure
print("\n--- Game Tree Structure ---")
game_tree.print_tree()

print("\n--- End of Game Tree Example ---")

