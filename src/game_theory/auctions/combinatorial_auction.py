import itertools

class CombinatorialAuction:
    def __init__(self, bidders, items):
        self.bidders = bidders  # List of GameAgent objects
        self.items = items      # List of available items (e.g., ["itemA", "itemB"])
        self.bids = []          # List of submitted bids: [(bidder, bundle, bid_amount)]

    def submit_bid(self, bidder, bundle, bid_amount):
        # bundle should be a frozenset of items
        if not isinstance(bundle, frozenset):
            bundle = frozenset(bundle)
        if not bundle.issubset(self.items):
            raise ValueError("Bundle contains items not in the auction.")
        if bidder not in self.bidders:
            raise ValueError("Bidder is not a registered bidder.")
        self.bids.append((bidder, bundle, bid_amount))

    def run_auction(self):
        if not self.bids:
            return {"allocation": {}, "revenue": 0, "message": "No bids submitted."}

        # This is a highly simplified allocation mechanism for demonstration.
        # A real combinatorial auction solver would use integer programming
        # to find the optimal allocation that maximizes revenue or social welfare.
        # For this example, we'll just pick the single highest bid for a non-overlapping bundle.

        best_allocation = {}
        max_revenue = 0

        # Sort bids by amount in descending order
        sorted_bids = sorted(self.bids, key=lambda x: x[2], reverse=True)

        allocated_items = set()

        for bidder, bundle, bid_amount in sorted_bids:
            # Check if any item in the bundle has already been allocated
            if not (bundle & allocated_items): # If no overlap
                if bid_amount > max_revenue: # Simple greedy approach for single highest bid
                    max_revenue = bid_amount
                    best_allocation = {bidder.name: list(bundle)}
                    allocated_items.update(bundle)
                    # In a real solver, we'd continue to find compatible bids
                    # but for this simplification, we stop after finding the highest single non-overlapping bid
                    break 

        if max_revenue > 0:
            return {"allocation": best_allocation, "revenue": max_revenue, "message": "Auction concluded successfully (simplified allocation)."}
        else:
            return {"allocation": {}, "revenue": 0, "message": "No valid allocation found."}
