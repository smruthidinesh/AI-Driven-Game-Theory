class VCGMechanism:
    def __init__(self, participants):
        self.participants = participants  # List of participants, each with a valuation

    def run_mechanism(self, bids):
        # Bids should be a dictionary: {participant_name: bid_value}
        if not bids:
            return {"winner": None, "price": 0, "message": "No bids received."}

        # Sort bids in descending order
        sorted_bids = sorted(bids.items(), key=lambda item: item[1], reverse=True)

        winner_name = sorted_bids[0][0]
        winner_bid = sorted_bids[0][1]

        # Calculate the VCG price (second-highest bid for a single item)
        if len(sorted_bids) > 1:
            price = sorted_bids[1][1]
        else:
            # If only one bidder, price is 0 (or a reserve price if defined)
            price = 0

        return {"winner": winner_name, "price": price, "winning_bid": winner_bid}

class Participant:
    def __init__(self, name, valuation):
        self.name = name
        self.valuation = valuation

    def submit_bid(self):
        # In a VCG mechanism, it's a dominant strategy to bid your true valuation
        return self.valuation
