import numpy as np
from src.game_theory.games.bayesian_game import BayesianGame
from src.game_theory.games.sequential_game import SequentialGame
from src.game_theory.games.prisoner_dilemma import PrisonerDilemma

class GameEnvironment:
    def __init__(self, game):
        self.game = game

class BayesianGameEnvironment(GameEnvironment):
    def __init__(self, game):
        super().__init__(game)
        self.state = None
        self.reset()

    def reset(self):
        # The state is the incumbent's type, chosen by nature
        self.state = np.random.choice(self.game.types["Incumbent"])
        return self.state

    def step(self, action):
        # The RL agent is the Entrant
        entrant_action = action
        incumbent_type = self.state

        # Incumbent's action is deterministic based on type
        if incumbent_type == "strong":
            incumbent_action = "Fight"
        else:
            incumbent_action = "Accommodate"

        # Get payoffs
        payoff_key = (entrant_action, incumbent_action, incumbent_type)
        entrant_payoff, _ = self.game.payoffs[payoff_key]

        # The game ends after one step
        done = True
        
        # The next state is irrelevant as the game is over
        next_state = self.reset()

        return next_state, entrant_payoff, done

    def get_state(self):
        return self.state

class SequentialGameEnvironment(GameEnvironment):
    def __init__(self, game: SequentialGame):
        super().__init__(game)
        self.current_round = 0
        self.pot = 0
        self.reset()

    def reset(self):
        self.current_round = 1
        self.pot = 1
        return (self.current_round, self.pot)

    def step(self, action):
        player = (self.current_round % 2) + 1 # Player 1 in odd rounds, Player 2 in even rounds
        reward = 0
        done = False

        if action == "Take":
            done = True
            if player == 1:
                reward = self.pot
            else:
                reward = self.pot
        elif action == "Pass":
            self.current_round += 1
            self.pot *= 2 # Pot doubles each round
            if self.current_round > self.game.rounds:
                done = True
                # If last player passes, both get 0
                reward = 0
        
        next_state = (self.current_round, self.pot) if not done else (self.game.rounds, 0)
        return next_state, reward, done

    def get_state(self):
        return (self.current_round, self.pot)

class PrisonerDilemmaEnvironment(GameEnvironment):
    def __init__(self, game: PrisonerDilemma):
        super().__init__(game)
        self.opponent_strategy = "Cooperate" # Simple opponent for RL agent
        self.reset()

    def reset(self):
        # State can be simplified for a single-round game or just a start state
        return "start"

    def step(self, action):
        # RL agent's action
        agent_action = action
        
        # Opponent's action (fixed for this simple environment)
        opponent_action = self.opponent_strategy

        # Get payoffs from the game
        payoff_key = (agent_action, opponent_action)
        agent_payoff, _ = self.game.payoff_matrix[payoff_key]

        done = True # Single round game
        next_state = "terminal" # Game ends

        return next_state, agent_payoff, done

    def get_state(self):
        return "start"
