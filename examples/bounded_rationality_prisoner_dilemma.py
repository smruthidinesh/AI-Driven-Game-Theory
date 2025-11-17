import sys
import os

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

from src.game_theory.games.prisoner_dilemma import PrisonerDilemma
from src.multi_agent.bounded_rational_agent import BoundedRationalAgent

print("--- Bounded Rational Agents playing Prisoner's Dilemma ---")

# Define possible actions for Prisoner's Dilemma
actions = ["Cooperate", "Defect"]

# Create two Bounded Rational Agents with Tit-for-Tat strategy and some error
agent1 = BoundedRationalAgent("Agent1", actions=actions, strategy="Tit-for-Tat", error_probability=0.05)
agent2 = BoundedRationalAgent("Agent2", actions=actions, strategy="Tit-for-Tat", error_probability=0.05)

game = PrisonerDilemma()

rounds = 20
total_payoff1 = 0
total_payoff2 = 0

print(f"Playing {rounds} rounds of Prisoner's Dilemma with Bounded Rational Agents...")

for i in range(rounds):
    # Agents choose actions based on their strategy and opponent's last action
    action1 = agent1.choose_action()
    action2 = agent2.choose_action()

    # Play a round of the game
    payoff1, payoff2 = game.play_round(action1, action2)

    # Agents observe opponent's action for the next round
    agent1.observe_opponent_action(action2)
    agent2.observe_opponent_action(action1)

    total_payoff1 += payoff1
    total_payoff2 += payoff2

    print(f"Round {i+1}: Agent1 chose {action1} (Payoff: {payoff1}), Agent2 chose {action2} (Payoff: {payoff2})")

print("\n--- Simulation Complete ---")
print(f"Total Payoff Agent 1: {total_payoff1}")
print(f"Total Payoff Agent 2: {total_payoff2}")
