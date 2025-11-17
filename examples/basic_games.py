from src.game_theory.games.prisoner_dilemma import PrisonerDilemma
from src.game_theory.games.battle_of_the_sexes import BattleOfTheSexes
from src.game_theory.games.chicken_game import ChickenGame
from src.game_theory.games.coordination_game import CoordinationGame
from src.multi_agent.agent import GameAgent

print("--- Running Prisoner's Dilemma Example ---")
game = PrisonerDilemma()
agent1 = GameAgent("Agent1", strategy="Defect")
agent2 = GameAgent("Agent2", strategy="Cooperate")
result = game.play_game(agent1, agent2, rounds=1)
print(f"Prisoner's Dilemma Payoffs: Agent1={result['average_payoff1']:.2f}, Agent2={result['average_payoff2']:.2f}")

print("\n--- Running Battle of the Sexes Example ---")
game = BattleOfTheSexes()
agent1 = GameAgent("Agent1", strategy="Opera")
agent2 = GameAgent("Agent2", strategy="Football")
result = game.play_game(agent1, agent2, rounds=1)
print(f"Battle of the Sexes Payoffs: Agent1={result['average_payoff1']:.2f}, Agent2={result['average_payoff2']:.2f}")

print("\n--- Running Chicken Game Example ---")
game = ChickenGame()
agent1 = GameAgent("Agent1", strategy="Swerve")
agent2 = GameAgent("Agent2", strategy="Straight")
result = game.play_game(agent1, agent2, rounds=1)
print(f"Chicken Game Payoffs: Agent1={result['average_payoff1']:.2f}, Agent2={result['average_payoff2']:.2f}")

print("\n--- Running Coordination Game Example ---")
game = CoordinationGame()
agent1 = GameAgent("Agent1", strategy="A")
agent2 = GameAgent("Agent2", strategy="B")
result = game.play_game(agent1, agent2, rounds=1)
print(f"Coordination Game Payoffs: Agent1={result['average_payoff1']:.2f}, Agent2={result['average_payoff2']:.2f}")
