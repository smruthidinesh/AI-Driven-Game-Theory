class NashEquilibrium:
    def __init__(self, game):
        self.game = game
        self.payoff_matrix = game.payoff_matrix
        self.player1_strategies = sorted(list(set([k[0] for k in self.payoff_matrix.keys()])))
        self.player2_strategies = sorted(list(set([k[1] for k in self.payoff_matrix.keys()])))

    def find_pure_strategy_equilibria(self):
        equilibria = []
        for s1 in self.player1_strategies:
            for s2 in self.player2_strategies:
                p1_payoff, p2_payoff = self.payoff_matrix[(s1, s2)]

                # Check if player 1 has an incentive to deviate
                p1_can_deviate = False
                for s1_alt in self.player1_strategies:
                    if s1_alt != s1:
                        alt_payoff, _ = self.payoff_matrix[(s1_alt, s2)]
                        if alt_payoff > p1_payoff:
                            p1_can_deviate = True
                            break
                
                if p1_can_deviate:
                    continue

                # Check if player 2 has an incentive to deviate
                p2_can_deviate = False
                for s2_alt in self.player2_strategies:
                    if s2_alt != s2:
                        _, alt_payoff = self.payoff_matrix[(s1, s2_alt)]
                        if alt_payoff > p2_payoff:
                            p2_can_deviate = True
                            break
                
                if not p2_can_deviate:
                    equilibria.append((s1, s2))
        return equilibria

    def find_mixed_strategy_equilibria(self):
        if len(self.player1_strategies) != 2 or len(self.player2_strategies) != 2:
            return [] # Only for 2x2 games for now

        s1_1, s1_2 = self.player1_strategies
        s2_1, s2_2 = self.player2_strategies

        a, e = self.payoff_matrix[(s1_1, s2_1)]
        b, f = self.payoff_matrix[(s1_1, s2_2)]
        c, g = self.payoff_matrix[(s1_2, s2_1)]
        d, h = self.payoff_matrix[(s1_2, s2_2)]

        # p is the probability of player 1 playing s1_1
        # q is the probability of player 2 playing s2_1
        
        # Player 2's indifference condition
        # p*e + (1-p)*g = p*f + (1-p)*h
        # p*(e-g-f+h) = h-g
        if (e - g - f + h) == 0:
            p = None # No unique solution
        else:
            p = (h - g) / (e - g - f + h)

        # Player 1's indifference condition
        # q*a + (1-q)*b = q*c + (1-q)*d
        # q*(a-b-c+d) = d-b
        if (a - b - c + d) == 0:
            q = None # No unique solution
        else:
            q = (d - b) / (a - b - c + d)

        if p is not None and q is not None and 0 < p < 1 and 0 < q < 1:
            return [({s1_1: p, s1_2: 1-p}, {s2_1: q, s2_2: 1-q})]
        else:
            return []
