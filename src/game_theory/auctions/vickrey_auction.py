class VickreyAuction:
    def __init__(self, bidders, items):
        self.bidders = bidders
        self.items = items

    def run_auction(self):
        bids = {}
        for bidder in self.bidders:
            bids[bidder] = bidder.get_bid(auction_type='vickrey')

        if not bids:
            return {"winner": None, "price": 0}

        sorted_bids = sorted(bids.items(), key=lambda item: item[1], reverse=True)
        
        winner = sorted_bids[0][0]
        if len(sorted_bids) > 1:
            price = sorted_bids[1][1]
        else:
            price = 0 # or some reserve price

        return {"winner": winner.name, "price": price}
