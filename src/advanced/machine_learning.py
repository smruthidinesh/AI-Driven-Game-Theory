import numpy as np
import random

class RLAgent:
    def __init__(self, name, actions):
        self.name = name
        self.actions = actions
        self.q_table = {}

    def get_q_value(self, state, action):
        return self.q_table.get((state, action), 0.0)

    def act(self, state, epsilon=0.1):
        if random.uniform(0, 1) < epsilon:
            return random.choice(self.actions)  # Explore
        else:
            q_values = [self.get_q_value(state, a) for a in self.actions]
            return self.actions[np.argmax(q_values)]  # Exploit

    def learn(self, state, action, reward, next_state, alpha=0.1, gamma=0.9):
        old_q_value = self.get_q_value(state, action)
        next_max_q = max([self.get_q_value(next_state, a) for a in self.actions])
        
        new_q_value = (1 - alpha) * old_q_value + alpha * (reward + gamma * next_max_q)
        self.q_table[(state, action)] = new_q_value

    def train(self, env, episodes=1000):
        print(f"--- Training RL Agent: {self.name} ---")
        for i in range(episodes):
            state = env.reset()
            done = False
            while not done:
                action = self.act(state)
                next_state, reward, done = env.step(action)
                self.learn(state, action, reward, next_state)
                state = next_state
            if (i + 1) % 100 == 0:
                print(f"Episode {i + 1}/{episodes} completed.")
        print("Training complete.")
