from src.multi_agent.agent import GameAgent

class RepeatedGame:
    def __init__(self, base_game, rounds):
        self.base_game = base_game
        self.rounds = rounds

    def play_game(self, agent1, agent2):
        total_payoff1 = 0
        total_payoff2 = 0
        payoffs_history1 = []
        payoffs_history2 = []

        for _ in range(self.rounds):
            # For simplicity, agents use their initial strategy throughout
            # More advanced implementations would allow strategies to evolve
            strategy1 = agent1.strategy
            strategy2 = agent2.strategy

            payoff1, payoff2 = self.base_game.play_round(strategy1, strategy2)
            total_payoff1 += payoff1
            total_payoff2 += payoff2
            payoffs_history1.append(payoff1)
            payoffs_history2.append(payoff2)

        return {
            "total_payoff1": total_payoff1,
            "total_payoff2": total_payoff2,
            "payoffs_history1": payoffs_history1,
            "payoffs_history2": payoffs_history2,
        }
