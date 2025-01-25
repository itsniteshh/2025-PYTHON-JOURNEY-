from art import logo
import os

print(logo)
print("Welcome to the Secret Auction Program!")


# TODO-2: Save data into dictionary {name: price}
blind_auction = {}

# TODO-3: Whether if new bids need to be added
end_of_game = True
highest_bid = 0
highest_bidder = ""

while end_of_game:

# TODO-1: Ask the user for input
    name = input("Enter your name?: ").capitalize()
    bid = int(input("What's your bid?: "))
    
# TODO-2: Save data into dictionary {name: price}
    blind_auction[name] = bid
    
    another_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    
    # TODO-4: Comparing bids in dictionary
    for names, amount in blind_auction.items():
        if amount > highest_bid:
            highest_bid = amount
            highest_bidder = names
            
    if another_bidder == "no":
        print(f"{highest_bidder} wins this game with his bid of {highest_bid}.")
        end_of_game = False
    else:
        os.system("cls" if os.name == "nt" else "clear")



