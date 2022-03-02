"""Silent Auction
Created by Francis Torcuato
24/02/2022
"""

def auction_rotation():
# Main Routine
item = input("What is the auction for? ")
reserve_price = float(input("What is the reserve price? "))
print(f"The auction for the {item} has started: ")
highest_bid = 0
enter_bid = input("What is your bid? ")
while enter_bid != -1:
enter_bid = input("What is your bid? ")


