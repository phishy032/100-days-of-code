from art import logo
print(logo)
print("Welcome to the secret auction program.")
bids = {}
finished = False

def find_highest_bidder (bid_dict):
    highest_bid = 0
    winner = ""
    for bidder in bid_dict:
        bid_amount = bid_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not finished:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    bids[name] = price
    more_bids = input("Are there any other bidders? Type 'yes' or 'no. ").lower()
    if more_bids == 'no':
        finished = True
        find_highest_bidder(bids)
    elif more_bids == 'yes':
        print("\n" * 100)

print(bids)
