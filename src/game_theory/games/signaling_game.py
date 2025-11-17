class SignalingGame:
    def __init__(self):
        self.name = "Simple Education Signaling Game"
        # Sender (Worker) types
        self.sender_types = {"High Ability": 0.5, "Low Ability": 0.5} # Prior probabilities
        # Sender (Worker) signals
        self.signals = ["Education", "No Education"]
        # Receiver (Employer) actions
        self.receiver_actions = ["High Wage", "Low Wage"]

        # Payoffs (Sender_Type, Signal, Receiver_Action) -> (Sender_Payoff, Receiver_Payoff)
        # This is a simplified representation for a specific game
        self.payoffs = {
            # High Ability Worker
            ("High Ability", "Education", "High Wage"): (3, 2), # Worker gets good job, Employer gets productive worker
            ("High Ability", "Education", "Low Wage"): (0, 1),  # Worker wasted effort, Employer gets productive worker cheaply
            ("High Ability", "No Education", "High Wage"): (2, 1), # Worker gets good job without effort, Employer might regret
            ("High Ability", "No Education", "Low Wage"): (1, 2), # Worker gets bad job, Employer avoids risk

            # Low Ability Worker
            ("Low Ability", "Education", "High Wage"): (-1, -1), # Worker wasted effort, Employer gets unproductive worker
            ("Low Ability", "Education", "Low Wage"): (-2, 0), # Worker wasted effort, Employer avoids big loss
            ("Low Ability", "No Education", "High Wage"): (0, -2), # Worker gets good job, Employer gets unproductive worker
            ("Low Ability", "No Education", "Low Wage"): (1, 1), # Worker gets bad job, Employer avoids risk
        }

    def solve(self):
        # This is a highly simplified example of finding a separating equilibrium
        # In a separating equilibrium, High Ability workers choose Education, Low Ability choose No Education
        # And Employer infers type correctly from signal.

        # Employer's beliefs:
        # If Education: believes worker is High Ability
        # If No Education: believes worker is Low Ability

        # Employer's best response:
        # If Education (believes High Ability): Offer High Wage (2 > 1 for High Ability)
        # If No Education (believes Low Ability): Offer Low Wage (1 > -2 for Low Ability)

        # Worker's best response given employer's actions:
        # High Ability Worker:
        #   If Education -> High Wage: Payoff = 3
        #   If No Education -> Low Wage: Payoff = 1
        #   Chooses Education (3 > 1)

        # Low Ability Worker:
        #   If Education -> Low Wage: Payoff = -2
        #   If No Education -> Low Wage: Payoff = 1
        #   Chooses No Education (1 > -2)

        # This constitutes a separating equilibrium.
        return {
            "Equilibrium Type": "Separating Equilibrium",
            "High Ability Worker Strategy": "Education",
            "Low Ability Worker Strategy": "No Education",
            "Employer Response to Education": "High Wage",
            "Employer Response to No Education": "Low Wage"
        }
