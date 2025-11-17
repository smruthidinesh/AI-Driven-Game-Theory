class SequentialGame:
    def __init__(self, name, rounds=4):
        self.name = name
        self.rounds = rounds

    def solve(self):
        # Solves the Centipede Game using backward induction
        
        # At the last round, the player will always choose to take the pot.
        # Payoffs at round n: (n, n-1) if player n takes, (n-1, n+1) if player n passes
        # For the last player, taking is always better.
        
        # Let's analyze the last decision at round self.rounds
        # Player is (self.rounds % 2) + 1
        # Payoff to take: (self.rounds, self.rounds-2) for player 1 if rounds is even
        # Payoff to take: (self.rounds-1, self.rounds) for player 2 if rounds is odd
        # The logic of backward induction means the first player will always take the pot.
        
        return {
            "equilibrium_strategy": "Player 1 takes at the first opportunity",
            "payoffs": (1, 0)
        }
