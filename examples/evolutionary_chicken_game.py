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

from src.game_theory.games.chicken_game import ChickenGame
from src.multi_agent.evolutionary_agent import EvolutionaryPopulation

if __name__ == "__main__":
    # Initialize the game
    game = ChickenGame()

    # Define parameters for the evolutionary simulation
    population_size = 20
    strategy_length = 1 # For Chicken Game, a simple strategy (Swerve/Straight) is enough
    mutation_rate = 0.1
    crossover_rate = 0.7
    generations = 50

    # Define possible actions for Chicken Game
    actions = ["Swerve", "Straight"]

    # Initialize the evolutionary population
    evolutionary_pop = EvolutionaryPopulation(
        game=game,
        actions=actions, # Pass actions to the population
        population_size=population_size,
        strategy_length=strategy_length,
        mutation_rate=mutation_rate,
        crossover_rate=crossover_rate
    )

    print("\n--- Evolutionary Chicken Game Simulation ---")
    # Evolve the population
    best_agent = evolutionary_pop.evolve(generations)

    print(f"\nAfter {generations} generations, the best agent has strategy: {best_agent.strategy} and fitness: {best_agent.fitness:.2f}")
