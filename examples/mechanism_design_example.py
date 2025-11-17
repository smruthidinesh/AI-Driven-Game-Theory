from src.advanced.mechanism_design import VCGMechanism, Participant

print("--- Mechanism Design Example: VCG Mechanism for Single Item ---")

# 1. Define Participants with their true valuations
participant1 = Participant("Alice", 100)
participant2 = Participant("Bob", 120)
participant3 = Participant("Charlie", 90)

participants = [participant1, participant2, participant3]

# 2. Participants submit their bids (true valuations in VCG)
bids = {p.name: p.submit_bid() for p in participants}
print(f"\nBids received: {bids}")

# 3. Create and run the VCG Mechanism
vco_mechanism = VCGMechanism(participants)
result = vco_mechanism.run_mechanism(bids)

print("\n--- Mechanism Result ---")
if result["winner"]:
    print(f"Winner: {result['winner']}")
    print(f"Winning Bid: {result['winning_bid']}")
    print(f"Price Paid (Vickrey Price): {result['price']}")
else:
    print(result["message"])

print("\n--- End of Mechanism Design Example ---")

