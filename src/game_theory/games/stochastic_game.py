import numpy as np

class StochasticGame:
    def __init__(self, name, states, actions_p1, actions_p2, transitions, rewards):
        self.name = name
        self.states = states  # List of states (e.g., ["S1", "S2"])
        self.actions_p1 = actions_p1  # List of actions for Player 1
        self.actions_p2 = actions_p2  # List of actions for Player 2
        self.transitions = transitions  # (state, action_p1, action_p2) -> {next_state: probability}
        self.rewards = rewards  # (state, action_p1, action_p2) -> (reward_p1, reward_p2)
        self.current_state = None

    def reset(self):
        self.current_state = np.random.choice(self.states) # Start in a random state
        return self.current_state

    def step(self, action_p1, action_p2):
        if self.current_state is None:
            raise ValueError("Game not reset. Call reset() first.")

        # Get rewards for current state and actions
        reward_p1, reward_p2 = self.rewards[(self.current_state, action_p1, action_p2)]

        # Determine next state based on probabilistic transitions
        possible_next_states_probs = self.transitions.get((self.current_state, action_p1, action_p2), {self.current_state: 1.0})
        
        next_state = np.random.choice(
            list(possible_next_states_probs.keys()),
            p=list(possible_next_states_probs.values())
        )
        self.current_state = next_state

        return next_state, reward_p1, reward_p2

    def play_game(self, agent1, agent2, episodes=1, steps_per_episode=10):
        print(f"\n--- Playing Stochastic Game: {self.name} ---")
        total_rewards_p1 = 0
        total_rewards_p2 = 0

        for episode in range(episodes):
            state = self.reset()
            print(f"Episode {episode + 1}: Initial State: {state}")
            episode_reward_p1 = 0
            episode_reward_p2 = 0

            for step in range(steps_per_episode):
                # Agents choose actions (for simplicity, random actions for now)
                action_p1 = np.random.choice(self.actions_p1)
                action_p2 = np.random.choice(self.actions_p2)

                next_state, reward_p1, reward_p2 = self.step(action_p1, action_p2)
                episode_reward_p1 += reward_p1
                episode_reward_p2 += reward_p2

                print(f"  Step {step + 1}: State {state}, P1 Action {action_p1}, P2 Action {action_p2}, Next State {next_state}, P1 Reward {reward_p1}, P2 Reward {reward_p2}")
                state = next_state
            
            total_rewards_p1 += episode_reward_p1
            total_rewards_p2 += episode_reward_p2
            print(f"Episode {episode + 1} Total Rewards: P1={episode_reward_p1}, P2={episode_reward_p2}")

        print(f"\nOverall Average Rewards per Episode: P1={total_rewards_p1/episodes:.2f}, P2={total_rewards_p2/episodes:.2f}")
        return {"average_reward_p1": total_rewards_p1/episodes, "average_reward_p2": total_rewards_p2/episodes}
