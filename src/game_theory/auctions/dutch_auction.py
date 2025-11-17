class DutchAuction:
    def __init__(self, bidders, items, start_price=200, decrement=5):
        self.bidders = bidders
        self.items = items
        self.start_price = start_price
        self.decrement = decrement

    def run_auction(self):
        current_price = self.start_price

        while current_price > 0:
            for bidder in self.bidders:
                if bidder.accept_price(current_price):
                    return {"winner": bidder.name, "price": current_price}
            current_price -= self.decrement

        return {"winner": None, "price": 0}
