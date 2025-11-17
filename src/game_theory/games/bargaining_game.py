class BargainingGame:
    def __init__(self, player1_utility_function, player2_utility_function, disagreement_point=(0, 0)):
        self.player1_utility_function = player1_utility_function
        self.player2_utility_function = player2_utility_function
        self.disagreement_point = disagreement_point

    def solve_nash_bargaining_solution(self):
        # For simplicity, assume linear utility functions and a fixed surplus to divide (e.g., 1 unit)
        # This is a highly simplified example and assumes specific utility forms

        # The Nash Bargaining Solution maximizes the product of the players' utilities
        # above their disagreement point: max (u1 - d1) * (u2 - d2)

        # Let's assume a simple scenario where players are dividing a surplus S=1
        # Player 1 gets x, Player 2 gets 1-x
        # Utility functions are linear: u1(x) = x, u2(1-x) = 1-x
        # Disagreement point d1, d2

        d1, d2 = self.disagreement_point

        # We want to maximize (x - d1) * ( (1-x) - d2 )
        # This is a quadratic function. We can find the maximum by taking the derivative and setting to zero.
        # Let f(x) = (x - d1) * (1 - x - d2)
        # f(x) = x - x^2 - x*d2 - d1 + d1*x + d1*d2
        # f'(x) = 1 - 2x - d2 + d1 = 0
        # 2x = 1 - d2 + d1
        # x = (1 + d1 - d2) / 2

        # Ensure x is within [0, 1]
        x_nash = (1 + d1 - d2) / 2
        x_nash = max(0, min(1, x_nash))

        u1_nash = self.player1_utility_function(x_nash)
        u2_nash = self.player2_utility_function(1 - x_nash)

        return {
            "solution_type": "Nash Bargaining Solution",
            "player1_share": x_nash,
            "player2_share": 1 - x_nash,
            "player1_utility": u1_nash,
            "player2_utility": u2_nash
        }
