"""Silent Auction
Created by Francis Torcuato
24/02/2022
"""


# Main Routine
item = input("What is the auction for? ")
reserve_price = float(input("What is the reserve price? "))
print(f"The auction for the {item} has started: ")
highest_bid = 0
enter_bid = 0
while enter_bid != -1:
    enter_bid = float(input("What is your bid? "))
    if highest_bid > enter_bid:
        print("Please enter the highest bid: ")
        print(f"highest bid so far is ${highest_bid}")
    else:
        print(f"Highest bid so far is ${enter_bid}")
        highest_bid = enter_bid

if highest_bid >= reserve_price:
    print(f"The auction for the {item} finished with a bid of ${highest_bid}")
else:
    print(f"The {item} didn't sell ")



