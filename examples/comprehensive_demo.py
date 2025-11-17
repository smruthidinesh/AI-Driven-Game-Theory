# This script provides a comprehensive demonstration of the project's features.

import matplotlib.pyplot as plt
from src.game_theory.games.prisoner_dilemma import PrisonerDilemma
from src.game_theory.games.battle_of_the_sexes import BattleOfTheSexes
from src.multi_agent.agent import GameAgent
from src.game_theory.auctions.english_auction import EnglishAuction
from src.game_theory.equilibria.nash_equilibrium import NashEquilibrium

print("--- 1. Game Simulation: Prisoner's Dilemma ---")
game = PrisonerDilemma()
agent1 = GameAgent("Agent1", strategy="Defect")
agent2 = GameAgent("Agent2", strategy="Cooperate")

rounds = 20
payoffs1 = []
payoffs2 = []

for _ in range(rounds):
    strategy1 = agent1.strategy
    strategy2 = agent2.strategy
    payoff1, payoff2 = game.play_round(strategy1, strategy2)
    payoffs1.append(payoff1)
    payoffs2.append(payoff2)

print(f"Prisoner's Dilemma Payoffs after {rounds} rounds:")
print(f"  Agent1 (Defect): {sum(payoffs1)}")
print(f"  Agent2 (Cooperate): {sum(payoffs2)}")

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(payoffs1, label="Agent 1 (Defect)")
plt.plot(payoffs2, label="Agent 2 (Cooperate)")
plt.xlabel("Round")
plt.ylabel("Payoff")
plt.title("Prisoner's Dilemma Payoffs Over Time")
plt.legend()
plt.grid(True)
plt.savefig("prisoner_dilemma_payoffs.png")
print("\nPlot saved to prisoner_dilemma_payoffs.png")

print("\n--- 2. Auction Simulation: English Auction ---")
agent3 = GameAgent("Agent3", strategy=None, valuation=100)
agent4 = GameAgent("Agent4", strategy=None, valuation=120)
bidders = [agent3, agent4]
items = ["item1"]
auction = EnglishAuction(bidders, items)
result = auction.run_auction()
print(f"English Auction Winner: {result['winner']}, Price: {result['price']}")

print("\n--- 3. Equilibrium Calculation: Battle of the Sexes ---")
game = BattleOfTheSexes()
ne = NashEquilibrium(game)
pure_equilibria = ne.find_pure_strategy_equilibria()
print(f"Pure Strategy Nash Equilibria for Battle of the Sexes: {pure_equilibria}")

mixed_equilibria = ne.find_mixed_strategy_equilibria()
print(f"Mixed Strategy Nash Equilibria for Battle of the Sexes: {mixed_equilibria}")
