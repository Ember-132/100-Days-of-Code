logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

continue_bid = True
bids = {}

while continue_bid:
    print("Welcome to the silent auction program")
    name = input("What is your name? ")
    bid = input("What is your bid?: £")
    bids[name] = bid
    next_bidder = input('Are there any other bidders? Type "yes" or "no" ')
    if next_bidder == "no":
        continue_bid = False
    else:
        print("\n" * 100)

max_bid = 0
max_bidder = ""
for bidder in bids:
    if int(bids[bidder]) > int(max_bid):
        max_bid = (bids[bidder])
        max_bidder = bidder

print(f"The max bid was {max_bidder} with £{max_bid}")



