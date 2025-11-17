from src.game_theory.auctions.first_price_sealed_bid_auction import FirstPriceSealedBidAuction
from src.multi_agent.agent import GameAgent

print("--- First-Price Sealed-Bid Auction Example ---")
# Create bidders with valuations (though not directly used by the auction mechanism itself)
# Provide a dummy strategy for GameAgent as it's a required argument
agent_a = GameAgent("AgentA", strategy=None, valuation=100)
agent_b = GameAgent("AgentB", strategy=None, valuation=120)
agent_c = GameAgent("AgentC", strategy=None, valuation=90)

bidders = [agent_a, agent_b, agent_c]
items = ["item1"]

auction = FirstPriceSealedBidAuction(bidders, items)

# Agents submit their bids
auction.submit_bid(agent_a, 95)
auction.submit_bid(agent_b, 110)
auction.submit_bid(agent_c, 95)

result = auction.run_auction()
print(f"Winner: {result['winner']}, Price: {result['price']}")
print(f"Message: {result['message']}")