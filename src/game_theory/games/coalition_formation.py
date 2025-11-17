import itertools

class CoalitionFormationGame:
    def __init__(self, players, characteristic_function):
        self.players = players  # List of player identifiers (e.g., [1, 2, 3])
        self.characteristic_function = characteristic_function  # Function v(S) -> value of coalition S

    def get_all_coalitions(self):
        all_coalitions = []
        for i in range(1, len(self.players) + 1):
            for subset in itertools.combinations(self.players, i):
                all_coalitions.append(frozenset(subset))
        return all_coalitions

    def find_core(self):
        # A very simplified approach to finding the core for a small number of players
        # The core is the set of imputations (payoff distributions) that are:
        # 1. Individually rational (each player gets at least their solo value)
        # 2. Group rational (each coalition gets at least its value)
        # 3. Feasible (sum of payoffs equals the grand coalition value)

        # This implementation will only check for feasibility and group rationality for a few simple cases.
        # A full implementation of the core is computationally intensive.

        n = len(self.players)
        if n > 3: # Core computation becomes very complex quickly
            return "Core computation for >3 players is complex and not implemented in this simplified version."

        grand_coalition = frozenset(self.players)
        v_N = self.characteristic_function(grand_coalition)

        # For a 2-player game, the core is simply any imputation (x1, x2) such that:
        # x1 >= v({1}), x2 >= v({2}), and x1 + x2 = v({1,2})
        if n == 2:
            v1 = self.characteristic_function(frozenset([self.players[0]]))
            v2 = self.characteristic_function(frozenset([self.players[1]]))
            
            if v_N >= v1 + v2:
                return f"Core exists. Player 1 gets at least {v1}, Player 2 gets at least {v2}. Total {v_N}."
            else:
                return "Core is empty (grand coalition value is less than sum of individual values)."

        # For a 3-player game, the conditions are more involved.
        # This simplified version will just state the conditions.
        if n == 3:
            return "For 3 players, the core requires checking individual and all sub-coalition rationality. This simplified version does not compute it directly."

        return "No specific core logic for this number of players in simplified version."
