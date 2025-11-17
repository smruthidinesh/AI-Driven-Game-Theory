from src.multi_agent.evolutionary_agent import EvolutionaryAgent

class ChickenGame:
    def __init__(self):
        self.payoff_matrix = {
            ("Swerve", "Swerve"): (0, 0),
            ("Swerve", "Straight"): (-1, 1),
            ("Straight", "Swerve"): (1, -1),
            ("Straight", "Straight"): (-10, -10),
        }

    def play_round(self, strategy1, strategy2):
        return self.payoff_matrix[(strategy1, strategy2)]

    def play_game(self, agent1, agent2, rounds):
        total_payoff1 = 0
        total_payoff2 = 0

        for r in range(rounds):
            # Determine action for agent 1
            if hasattr(agent1, 'play_action'):
                action1 = agent1.play_action(r)
            else:
                action1 = agent1.strategy

            # Determine action for agent 2
            if hasattr(agent2, 'play_action'):
                action2 = agent2.play_action(r)
            else:
                action2 = agent2.strategy

            payoff1, payoff2 = self.play_round(action1, action2)
            total_payoff1 += payoff1
            total_payoff2 += payoff2

        return {
            "average_payoff1": total_payoff1 / rounds,
            "average_payoff2": total_payoff2 / rounds,
        }
