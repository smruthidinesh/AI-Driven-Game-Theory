import numpy as np
from src.multi_agent.agent import GameAgent

class CournotFirm(GameAgent):
    def __init__(self, name, cost_per_unit):
        super().__init__(name, strategy=None) # Strategy will be quantity produced
        self.cost_per_unit = cost_per_unit
        self.quantity = 0

    def set_quantity(self, quantity):
        self.quantity = quantity

    def calculate_profit(self, market_price):
        revenue = market_price * self.quantity
        cost = self.cost_per_unit * self.quantity
        return revenue - cost

def market_price_function(total_quantity, demand_intercept=100, demand_slope=1):
    # Simple linear demand function: P = a - bQ
    price = demand_intercept - demand_slope * total_quantity
    return max(0, price) # Price cannot be negative

if __name__ == "__main__":
    print("--- Case Study: Cournot Oligopoly Competition ---")

    # 1. Define Firms (Players)
    firm1 = CournotFirm("Firm A", cost_per_unit=10)
    firm2 = CournotFirm("Firm B", cost_per_unit=12)
    firm3 = CournotFirm("Firm C", cost_per_unit=11)

    firms = [firm1, firm2, firm3]

    # 2. Simulate Competition (simplified for demonstration)
    # In a real Cournot model, firms would choose quantities simultaneously
    # and iteratively adjust to find equilibrium. Here, we'll just set quantities.

    # Example quantities chosen by firms
    firm1.set_quantity(20)
    firm2.set_quantity(15)
    firm3.set_quantity(18)

    # Calculate total quantity in the market
    total_quantity = sum(firm.quantity for firm in firms)
    print(f"\nTotal quantity produced: {total_quantity}")

    # Calculate market price
    market_price = market_price_function(total_quantity)
    print(f"Market price: {market_price:.2f}")

    # Calculate profits for each firm
    print("\nFirm Profits:")
    for firm in firms:
        profit = firm.calculate_profit(market_price)
        print(f"{firm.name} (Quantity: {firm.quantity}): Profit = {profit:.2f}")

    print("\n--- End of Case Study ---")
