import random
import numpy as np

class EvolutionaryAgent:
    def __init__(self, actions, strategy_length, initial_strategy=None):
        self.actions = actions # Store possible actions
        self.strategy_length = strategy_length
        if initial_strategy is None:
            # Represent strategy as a binary string (e.g., 0 for first action, 1 for second)
            self.strategy = [random.randint(0, len(actions) - 1) for _ in range(strategy_length)]
        else:
            self.strategy = initial_strategy
        self.fitness = 0

    def play_action(self, round_num):
        # Use the strategy (index) to pick an action from the provided actions list
        action_index = self.strategy[round_num % self.strategy_length]
        return self.actions[action_index]

    def __repr__(self):
        return f"Agent(Strategy={self.strategy}, Fitness={self.fitness:.2f})"

class EvolutionaryPopulation:
    def __init__(self, game, actions, population_size, strategy_length, mutation_rate=0.01, crossover_rate=0.7):
        self.game = game
        self.actions = actions # Store possible actions for agents
        self.population_size = population_size
        self.strategy_length = strategy_length
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.population = [EvolutionaryAgent(actions, strategy_length) for _ in range(population_size)]

    def evaluate_fitness(self, rounds_per_game=10):
        for agent in self.population:
            agent.fitness = 0

        # Each agent plays against every other agent (or a subset)
        for i in range(self.population_size):
            for j in range(i + 1, self.population_size):
                agent1 = self.population[i]
                agent2 = self.population[j]

                total_payoff1 = 0
                total_payoff2 = 0

                for r in range(rounds_per_game):
                    action1 = agent1.play_action(r)
                    action2 = agent2.play_action(r)
                    payoff1, payoff2 = self.game.play_round(action1, action2)
                    total_payoff1 += payoff1
                    total_payoff2 += payoff2
                
                agent1.fitness += total_payoff1
                agent2.fitness += total_payoff2

    def select_parents(self):
        # Tournament selection
        tournament_size = 3
        parents = []
        for _ in range(2): # Select two parents
            tournament_contenders = random.sample(self.population, tournament_size)
            winner = max(tournament_contenders, key=lambda agent: agent.fitness)
            parents.append(winner)
        return parents[0], parents[1]

    def crossover(self, parent1, parent2):
        if self.strategy_length <= 1: # No meaningful crossover for strategy length 1 or less
            return EvolutionaryAgent(self.actions, self.strategy_length, parent1.strategy), EvolutionaryAgent(self.actions, self.strategy_length, parent2.strategy)

        if random.random() < self.crossover_rate:
            crossover_point = random.randint(1, self.strategy_length - 1)
            child1_strategy = parent1.strategy[:crossover_point] + parent2.strategy[crossover_point:]
            child2_strategy = parent2.strategy[:crossover_point] + parent1.strategy[crossover_point:]
            return EvolutionaryAgent(self.actions, self.strategy_length, child1_strategy), EvolutionaryAgent(self.actions, self.strategy_length, child2_strategy)
        return EvolutionaryAgent(self.actions, self.strategy_length, parent1.strategy), EvolutionaryAgent(self.actions, self.strategy_length, parent2.strategy)

    def mutate(self, agent):
        for i in range(self.strategy_length):
            if random.random() < self.mutation_rate:
                agent.strategy[i] = 1 - agent.strategy[i] # Flip the bit
        return agent

    def evolve(self, generations):
        for gen in range(generations):
            self.evaluate_fitness()
            new_population = []

            # Keep the best agent (elitism)
            best_agent = max(self.population, key=lambda agent: agent.fitness)
            new_population.append(EvolutionaryAgent(self.actions, self.strategy_length, list(best_agent.strategy)))

            while len(new_population) < self.population_size:
                parent1, parent2 = self.select_parents()
                child1, child2 = self.crossover(parent1, parent2)
                new_population.append(self.mutate(child1))
                if len(new_population) < self.population_size:
                    new_population.append(self.mutate(child2))
            
            self.population = new_population
            print(f"Generation {gen+1}: Best Fitness = {best_agent.fitness:.2f}, Best Strategy = {best_agent.strategy}")

        self.evaluate_fitness() # Final evaluation
        return max(self.population, key=lambda agent: agent.fitness)
