from src.multi_agent.bounded_rational_agent import BoundedRationalAgent

class BattleOfTheSexes:
    def __init__(self):
        self.payoff_matrix = {
            ("Opera", "Opera"): (3, 2),
            ("Opera", "Football"): (0, 0),
            ("Football", "Opera"): (0, 0),
            ("Football", "Football"): (2, 3),
        }

    def play_round(self, strategy1, strategy2):
        return self.payoff_matrix[(strategy1, strategy2)]

    def play_game(self, agent1, agent2, rounds):
        total_payoff1 = 0
        total_payoff2 = 0

        for _ in range(rounds):
            # Determine action for agent 1
            if hasattr(agent1, 'choose_action') and hasattr(agent1, 'observe_opponent_action'):
                action1 = agent1.choose_action()
            else:
                action1 = agent1.strategy

            # Determine action for agent 2
            if hasattr(agent2, 'choose_action') and hasattr(agent2, 'observe_opponent_action'):
                action2 = agent2.choose_action()
            else:
                action2 = agent2.strategy

            payoff1, payoff2 = self.play_round(action1, action2)
            total_payoff1 += payoff1
            total_payoff2 += payoff2

            # Agents observe opponent's action
            if hasattr(agent1, 'observe_opponent_action'):
                agent1.observe_opponent_action(action2)
            if hasattr(agent2, 'observe_opponent_action'):
                agent2.observe_opponent_action(action1)

        return {
            "average_payoff1": total_payoff1 / rounds,
            "average_payoff2": total_payoff2 / rounds,
        }
