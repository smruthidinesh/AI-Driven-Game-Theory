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
from src.multi_agent.evolutionary_agent import EvolutionaryPopulation

print("--- Evolutionary Agents evolving strategies for Prisoner's Dilemma ---")

game = PrisonerDilemma()

population_size = 20
strategy_length = 5 # Length of the strategy (e.g., sequence of actions)
mutation_rate = 0.1
crossover_rate = 0.7
generations = 50

# Define possible actions for Prisoner's Dilemma
actions = ["Cooperate", "Defect"]

population = EvolutionaryPopulation(
    game=game,
    actions=actions, # Pass actions to the population
    population_size=population_size,
    strategy_length=strategy_length,
    mutation_rate=mutation_rate,
    crossover_rate=crossover_rate
)

print(f"\nEvolving strategies for {generations} generations...")
best_agent = population.evolve(generations)

print("\n--- Evolution Complete ---")
print(f"Best strategy found: {best_agent.strategy} with fitness: {best_agent.fitness:.2f}")
print("Note: Strategy is represented as a binary sequence (0=Cooperate, 1=Defect).")
