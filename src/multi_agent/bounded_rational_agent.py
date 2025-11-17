import random
from src.multi_agent.agent import GameAgent

class BoundedRationalAgent(GameAgent):
    def __init__(self, name, actions, strategy="Tit-for-Tat", error_probability=0.1, valuation=100):
        super().__init__(name, strategy, valuation)
        self.actions = actions # Store possible actions
        self.error_probability = error_probability
        self.opponent_last_action = None # To store the opponent's last action

    def choose_action(self):
        # Implement a simple bounded rational strategy, e.g., Tit-for-Tat with error
        action = None
        if self.strategy == "Tit-for-Tat" and self.opponent_last_action is not None:
            action = self.opponent_last_action
        elif self.strategy in self.actions: # If strategy is one of the valid actions
            action = self.strategy
        else: # Default or unknown strategy, choose randomly from available actions
            action = random.choice(self.actions)

        # Introduce error/bounded rationality
        if random.random() < self.error_probability:
            # Make a mistake: choose a different action from the available actions
            other_actions = [a for a in self.actions if a != action]
            if other_actions: # Ensure there's an alternative to choose
                action = random.choice(other_actions)
            
        return action

    def observe_opponent_action(self, action):
        self.opponent_last_action = action
