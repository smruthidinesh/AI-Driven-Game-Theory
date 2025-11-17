# This script demonstrates the functionality of the game theory and auction modules.

from src.game_theory.games.prisoner_dilemma import PrisonerDilemma
from src.multi_agent.agent import GameAgent
from src.game_theory.auctions.english_auction import EnglishAuction

print("--- Running Game Theory Example ---")
game = PrisonerDilemma()
agent1 = GameAgent("Agent1", strategy="Defect")
agent2 = GameAgent("Agent2", strategy="Cooperate")

result = game.play_game(agent1, agent2, rounds=1)
print(f"Prisoner's Dilemma Payoffs: Agent1={result['average_payoff1']:.2f}, Agent2={result['average_payoff2']:.2f}")

print("\n--- Running Auction Example ---")

agent3 = GameAgent("Agent3", strategy=None, valuation=100)
agent4 = GameAgent("Agent4", strategy=None, valuation=120)
bidders = [agent3, agent4]
items = ["item1"]

auction = EnglishAuction(bidders, items)
result = auction.run_auction()
print(f"English Auction Winner: {result['winner']}, Price: {result['price']}")
