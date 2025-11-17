import numpy as np
from src.multi_agent.agent import GameAgent

class QLearningAgent(GameAgent):
    def __init__(self, name, actions, learning_rate=0.1, discount_factor=0.9, epsilon=0.1, strategy=None, valuation=100):
        super().__init__(name, strategy, valuation) # Call parent constructor
        self.actions = actions  # List of possible actions (e.g., ["Cooperate", "Defect"])
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.q_table = {}
        self.last_state = None
        self.last_action = None

    def get_q_value(self, state, action):
        return self.q_table.get((state, action), 0.0)

    def choose_action(self, state):
        self.last_state = state
        if np.random.uniform(0, 1) < self.epsilon: # Epsilon-greedy exploration
            self.last_action = np.random.choice(self.actions)
        else:
            q_values = [self.get_q_value(state, action) for action in self.actions]
            max_q = max(q_values)
            # Handle ties by choosing randomly among actions with max Q-value
            best_actions = [self.actions[i] for i, q in enumerate(q_values) if q == max_q]
            self.last_action = np.random.choice(best_actions)
        return self.last_action

    def learn(self, next_state, reward):
        if self.last_state is None or self.last_action is None:
            return # Cannot learn without previous state and action

        old_q_value = self.get_q_value(self.last_state, self.last_action)
        
        # Find max Q-value for the next state
        next_q_values = [self.get_q_value(next_state, action) for action in self.actions]
        max_next_q = max(next_q_values) if next_q_values else 0.0

        new_q_value = old_q_value + self.learning_rate * (
            reward + self.discount_factor * max_next_q - old_q_value
        )
        self.q_table[(self.last_state, self.last_action)] = new_q_value

    # Override get_bid to use Q-learning for action selection if applicable
    # For now, we'll assume choose_action is called directly by the game environment
    # or a wrapper.
