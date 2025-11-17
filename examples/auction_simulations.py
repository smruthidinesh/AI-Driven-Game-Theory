# This script demonstrates the functionality of the auction modules.

from src.multi_agent.agent import GameAgent
from src.game_theory.auctions.english_auction import EnglishAuction
from src.game_theory.auctions.dutch_auction import DutchAuction
from src.game_theory.auctions.vickrey_auction import VickreyAuction

print("--- Running English Auction Example ---")
agent1 = GameAgent("Agent1", strategy=None, valuation=100)
agent2 = GameAgent("Agent2", strategy=None, valuation=120)
bidders = [agent1, agent2]
items = ["item1"]

auction = EnglishAuction(bidders, items)
result = auction.run_auction()
print(f"English Auction Winner: {result['winner']}, Price: {result['price']}")

print("\n--- Running Dutch Auction Example ---")
agent3 = GameAgent("Agent3", strategy=None, valuation=130)
agent4 = GameAgent("Agent4", strategy=None, valuation=150)
bidders = [agent3, agent4]

auction = DutchAuction(bidders, items, start_price=200, decrement=10)
result = auction.run_auction()
print(f"Dutch Auction Winner: {result['winner']}, Price: {result['price']}")

print("\n--- Running Vickrey Auction Example ---")
agent5 = GameAgent("Agent5", strategy=None, valuation=110)
agent6 = GameAgent("Agent6", strategy=None, valuation=140)
bidders = [agent5, agent6]

auction = VickreyAuction(bidders, items)
result = auction.run_auction()
print(f"Vickrey Auction Winner: {result['winner']}, Price: {result['price']}")
