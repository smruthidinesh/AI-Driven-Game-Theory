from src.game_theory.auctions.all_pay_auction import AllPayAuction
from src.multi_agent.agent import GameAgent

print("\n--- All-Pay Auction Example ---")
# Provide a dummy strategy for GameAgent as it's a required argument
agent_x = GameAgent("AgentX", strategy=None, valuation=80)
agent_y = GameAgent("AgentY", strategy=None, valuation=90)
agent_z = GameAgent("AgentZ", strategy=None, valuation=75)

bidders = [agent_x, agent_y, agent_z]
items = ["trophy"]

auction = AllPayAuction(bidders, items)

# Agents submit their bids
auction.submit_bid(agent_x, 70)
auction.submit_bid(agent_y, 85)
auction.submit_bid(agent_z, 60)

result = auction.run_auction()
print(f"Winner: {result['winner']}, Price (highest bid): {result['price']}")
print(f"Payments: {result['payments']}")
print(f"Message: {result['message']}")