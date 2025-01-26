from art import logo
import os
import random

#TODO1: GETTING users two cards total and computers's first card
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def getting_cards(cards):
    """func to get 2 cards for user and 2 for com"""
    user_cards = []
    com_cards = []
    
    for i in range(3):
        user_rand = random.choice(cards)
        com_rand = random.choice(cards)
        
        user_cards.append(user_rand)
        com_cards.append(com_rand)      
    return user_cards, com_cards

user_deck, com_deck = getting_cards(cards)
first_hand = user_deck[:2]

#TODO2: Doing calculation
def calculation(user_dec, com_deck, another_card):
    
    if sum(first_hand) == 21 or sum(first_hand) == 20:
        return f"You Win!"

#TODO3: making sure the program runs
end_of_game = True

while end_of_game:
    os.system("cls" if os.name == "nt" else "clear")
    print(logo)
    print(f"Your cards: {first_hand}, current score: {first_hand[:2]}")
    print(f"Computer's first card: {com_deck[0]}")
    
    another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
