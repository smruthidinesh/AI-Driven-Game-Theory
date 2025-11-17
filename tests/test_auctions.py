import sys
import os
import pytest

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

print(f"Project Root added to sys.path: {project_root}")
print(f"Current sys.path: {sys.path}")

try:
    import src
    print("Successfully imported 'src' as a top-level package.")
except ImportError as e:
    print(f"Failed to import 'src' as a top-level package: {e}")

from src.game_theory.auctions.english_auction import EnglishAuction
from src.game_theory.auctions.dutch_auction import DutchAuction
from src.game_theory.auctions.vickrey_auction import VickreyAuction
from src.multi_agent.agent import GameAgent

def test_english_auction():
    agent1 = GameAgent("Agent1", strategy=None, valuation=100)
    agent2 = GameAgent("Agent2", strategy=None, valuation=120)
    bidders = [agent1, agent2]
    items = ["item1"]
    auction = EnglishAuction(bidders, items)
    result = auction.run_auction()
    assert result["winner"] == "Agent2"
    assert result["price"] == 100

def test_dutch_auction():
    agent1 = GameAgent("Agent1", strategy=None, valuation=100)
    agent2 = GameAgent("Agent2", strategy=None, valuation=120)
    bidders = [agent1, agent2]
    items = ["item1"]
    auction = DutchAuction(bidders, items, start_price=150, decrement=5)
    result = auction.run_auction()
    assert result["winner"] == "Agent2"
    assert result["price"] == 120

def test_vickrey_auction():
    agent1 = GameAgent("Agent1", strategy=None, valuation=100)
    agent2 = GameAgent("Agent2", strategy=None, valuation=120)
    bidders = [agent1, agent2]
    items = ["item1"]
    auction = VickreyAuction(bidders, items)
    result = auction.run_auction()
    assert result["winner"] == "Agent2"
    assert result["price"] == 100
