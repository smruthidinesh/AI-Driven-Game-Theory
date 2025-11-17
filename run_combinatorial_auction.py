from src.game_theory.auctions.combinatorial_auction import CombinatorialAuction
from src.multi_agent.agent import GameAgent

print("\n--- Combinatorial Auction Example ---")
# Provide a dummy strategy for GameAgent as it's a required argument
agent_1 = GameAgent("Agent1", strategy=None)
agent_2 = GameAgent("Agent2", strategy=None)

bidders = [agent_1, agent_2]
items = frozenset(["A", "B", "C"]) # Define available items

auction = CombinatorialAuction(bidders, items)

# Agents submit bids for bundles of items
auction.submit_bid(agent_1, frozenset(["A"]), 10)
auction.submit_bid(agent_1, frozenset(["B", "C"]), 18)
auction.submit_bid(agent_2, frozenset(["A", "B"]), 15)
auction.submit_bid(agent_2, frozenset(["C"]), 7)

result = auction.run_auction()
print(f"Allocation: {result['allocation']}")
print(f"Revenue: {result['revenue']}")
print(f"Message: {result['message']}")