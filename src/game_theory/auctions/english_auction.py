class EnglishAuction:
    def __init__(self, bidders, items):
        self.bidders = bidders
        self.items = items

    def run_auction(self):
        current_price = 0
        active_bidders = list(self.bidders)
        last_bid = 0

        while len(active_bidders) > 1:
            bids = {}
            for bidder in active_bidders:
                bid = bidder.get_bid(current_price)
                if bid is not None:
                    bids[bidder] = bid
            
            if not bids:
                # No one bid, end auction
                return {"winner": None, "price": current_price}

            highest_bid = max(bids.values())
            highest_bidders = [bidder for bidder, bid in bids.items() if bid == highest_bid]

            if len(highest_bidders) == 1:
                winner = highest_bidders[0]
                # Price is the second highest bid, or the current price if only one bid
                bids.pop(winner)
                second_highest_bid = max(bids.values()) if bids else current_price
                return {"winner": winner.name, "price": second_highest_bid}
            else:
                # Multiple bidders at the same price, continue auction with them
                active_bidders = highest_bidders
                current_price = highest_bid

        if active_bidders:
            return {"winner": active_bidders[0].name, "price": current_price}
        else:
            return {"winner": None, "price": current_price}
