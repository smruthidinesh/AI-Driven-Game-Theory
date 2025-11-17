class CoordinationGame:
    def __init__(self):
        self.payoff_matrix = {
            ("A", "A"): (1, 1),
            ("A", "B"): (0, 0),
            ("B", "A"): (0, 0),
            ("B", "B"): (1, 1),
        }

    def play_round(self, strategy1, strategy2):
        return self.payoff_matrix[(strategy1, strategy2)]

    def play_game(self, agent1, agent2, rounds):
        total_payoff1 = 0
        total_payoff2 = 0

        for _ in range(rounds):
            strategy1 = agent1.strategy
            strategy2 = agent2.strategy
            payoff1, payoff2 = self.play_round(strategy1, strategy2)
            total_payoff1 += payoff1
            total_payoff2 += payoff2

        return {
            "average_payoff1": total_payoff1 / rounds,
            "average_payoff2": total_payoff2 / rounds,
        }
