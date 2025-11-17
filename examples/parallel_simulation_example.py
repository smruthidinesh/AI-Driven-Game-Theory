import multiprocessing
import time
from src.game_theory.games.prisoner_dilemma import PrisonerDilemma
from src.multi_agent.agent import GameAgent

def run_single_simulation(simulation_id, rounds):
    game = PrisonerDilemma()
    agent1 = GameAgent(f"Agent{simulation_id}_1", strategy="Defect")
    agent2 = GameAgent(f"Agent{simulation_id}_2", strategy="Cooperate")
    
    result = game.play_game(agent1, agent2, rounds=rounds)
    return simulation_id, result["average_payoff1"], result["average_payoff2"]

if __name__ == "__main__":
    print("--- Parallel Simulation Example ---")

    num_simulations = 10
    rounds_per_simulation = 1000
    num_processes = multiprocessing.cpu_count() # Use all available CPU cores

    print(f"Running {num_simulations} simulations with {rounds_per_simulation} rounds each.")
    print(f"Using {num_processes} parallel processes.")

    start_time = time.time()

    with multiprocessing.Pool(processes=num_processes) as pool:
        # Map the run_single_simulation function to a list of arguments
        results = pool.starmap(run_single_simulation, [(i, rounds_per_simulation) for i in range(num_simulations)])

    end_time = time.time()

    total_payoff1 = 0
    total_payoff2 = 0

    print("\n--- Simulation Results ---")
    for sim_id, payoff1, payoff2 in results:
        print(f"Simulation {sim_id}: P1 Avg Payoff={payoff1:.2f}, P2 Avg Payoff={payoff2:.2f}")
        total_payoff1 += payoff1
        total_payoff2 += payoff2

    print(f"\nOverall Average Payoffs: P1={total_payoff1/num_simulations:.2f}, P2={total_payoff2/num_simulations:.2f}")
    print(f"Total time taken: {end_time - start_time:.2f} seconds")

    print("\n--- End of Parallel Simulation Example ---")
