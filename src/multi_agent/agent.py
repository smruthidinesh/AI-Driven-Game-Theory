class GameAgent:
    def __init__(self, name, strategy, valuation=100):
        self.name = name
        self.strategy = strategy
        self.valuation = valuation

    def get_bid(self, current_price=0, auction_type='english'):
        if auction_type == 'english':
            if current_price < self.valuation:
                return current_price + 10  # Simple bidding strategy
            else:
                return None  # Drop out of the auction
        elif auction_type == 'vickrey':
            return self.valuation

    def accept_price(self, current_price):
        return self.valuation >= current_price
