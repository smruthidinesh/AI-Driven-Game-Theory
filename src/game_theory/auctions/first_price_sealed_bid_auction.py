class FirstPriceSealedBidAuction:
    def __init__(self, bidders, items):
        self.bidders = bidders  # List of GameAgent objects with a 'valuation' attribute
        self.items = items      # List of items being auctioned (for simplicity, assume one item for now)
        self.bids = {}

    def submit_bid(self, agent, bid_amount):
        if agent in self.bidders:
            self.bids[agent] = bid_amount
        else:
            raise ValueError("Agent is not a registered bidder.")

    def run_auction(self):
        if not self.bids:
            return {"winner": None, "price": 0, "message": "No bids submitted."}

        # Find the highest bid
        highest_bid = -1
        winner = None
        
        # Handle ties: In a first-price sealed-bid auction, ties are usually broken randomly
        # For simplicity, we'll pick the first one encountered if multiple have the highest bid
        potential_winners = []

        for bidder, bid_amount in self.bids.items():
            if bid_amount > highest_bid:
                highest_bid = bid_amount
                potential_winners = [bidder]
            elif bid_amount == highest_bid:
                potential_winners.append(bidder)
        
        if potential_winners:
            # Randomly select a winner if there's a tie
            import random
            winner = random.choice(potential_winners)

        if winner:
            return {"winner": winner.name, "price": highest_bid, "message": "Auction concluded successfully."}
        else:
            return {"winner": None, "price": 0, "message": "No valid winner found."}
