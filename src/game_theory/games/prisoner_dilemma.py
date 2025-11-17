from src.multi_agent.q_learning_agent import QLearningAgent

class PrisonerDilemma:
    def __init__(self):
        self.payoff_matrix = {
            ("Cooperate", "Cooperate"): (-1, -1),
            ("Cooperate", "Defect"): (-3, 0),
            ("Defect", "Cooperate"): (0, -3),
            ("Defect", "Defect"): (-2, -2),
        }

    def play_round(self, strategy1, strategy2):
        return self.payoff_matrix[(strategy1, strategy2)]

    def play_game(self, agent1, agent2, rounds):
        total_payoff1 = 0
        total_payoff2 = 0

        # Initialize last actions for Q-learning state
        last_action1 = None
        last_action2 = None

        for _ in range(rounds):
            # Determine action for agent 1
            if hasattr(agent1, 'choose_action') and hasattr(agent1, 'learn'):
                state1 = last_action2 # State for agent1 is opponent's last action
                action1 = agent1.choose_action(state1)
            else:
                action1 = agent1.strategy

            # Determine action for agent 2
            if hasattr(agent2, 'choose_action') and hasattr(agent2, 'learn'):
                state2 = last_action1 # State for agent2 is opponent's last action
                action2 = agent2.choose_action(state2)
            else:
                action2 = agent2.strategy

            payoff1, payoff2 = self.play_round(action1, action2)
            total_payoff1 += payoff1
            total_payoff2 += payoff2

            # Agents learn from the outcome
            if hasattr(agent1, 'learn'):
                agent1.learn(action2, payoff1) # Next state for agent1 is opponent's current action
            if hasattr(agent2, 'learn'):
                agent2.learn(action1, payoff2) # Next state for agent2 is opponent's current action
            
            last_action1 = action1
            last_action2 = action2

        return {
            "average_payoff1": total_payoff1 / rounds,
            "average_payoff2": total_payoff2 / rounds,
        }
