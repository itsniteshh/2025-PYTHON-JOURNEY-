from art import logo
import os
import random

print(logo)

#TODO1: GETTING users two cards total and computers's first card
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def getting_two_cards(cards):
    """func to get 2 cards for user and 2 for com"""
    user_cards = []
    com_cards = []
    
    for i in range(2):
        user_rand = random.choice(cards)
        com_rand = random.choice(cards)
        
        user_cards.append(user_rand)
        com_cards.append(com_rand)  
            
    return user_cards, com_cards
user_deck, com_deck = getting_two_cards(cards)

def getting_single_cards(cards):
    
    single_card = random.choice(cards)
    return single_card

single_cards = getting_single_cards(cards)

#TODO2: Doing calculation
def calculation(first_user_deck, first_com_deck):
    
    if sum(user_deck) == 21:
        print("You wins!😊")
        end_of_game = False
    elif sum(com_deck) == 21:
        print("Com wins!😢")
    elif sum(user_deck) == sum(com_deck):
        print("Game Draw!")
        end_of_game = False
    elif sum(user_deck) > 21 and 11 in user_deck:
        user_deck.pop(11)
        user_deck.append(1)
        
        if sum(user_deck) > 21:
            print("BUST")
        elif sum(user_deck) > sum(com_deck):
            print("You win!😊")
            end_of_game = False
        else:
            print("You lose! Com wins 😢")
            end_of_game = False

#TODO3: making sure the program runs
end_of_game = True

while end_of_game:
    print(f"Your cards: {user_deck}, current score: {sum(user_deck)}")
    print(f"Computer's first card: {com_deck[0]}")

    another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    
    
    if another_card == "y":
        user_deck.append(single_cards)
        
        if sum(com_deck) <= 17:
            com_deck.append(single_cards)
            
    elif another_card == "n":
        print(f"Your final hand: {user_deck}, final_score: {sum(user_deck)}")
        print(f"Computer's final hand: {com_deck}, final score: {sum(com_deck)}")
        
        if sum(user_deck) == 21:
            print("You wins!👌")
            break
            
        elif sum(com_deck) == 21:
            print("Com wins!😢")
            break
            
        elif sum(user_deck) == sum(com_deck):
            print("Game Draw!")
            break
            
        else:
            if sum(user_deck) > 21 and 11 in user_deck:
                user_deck.pop(11)
                user_deck.append(1)
            
            if sum(user_deck) > 21:
                print("BUST")
                break
                
            elif sum(user_deck) > sum(com_deck):
                print("You win!😊")
                break
                
            else:
                print("You lose! Com wins 😢")
                break
            
        
    if sum(user_deck) == 21:
        print("You wins!😊")
        break
    
    elif sum(com_deck) == 21:
        print(f"Computer's final hand: {com_deck}, final score: {sum(com_deck)}")
        break
    
    elif sum(user_deck) == sum(com_deck):
        print("Game Draw!")
        break
    
    elif sum(user_deck) > 21 and 11 in user_deck:
        user_deck.pop(11)
        user_deck.append(1)
        
        if sum(user_deck) > 21:
            print("BUST")
            break
        
        elif sum(user_deck) > sum(com_deck):
            print("You win!😊")
            break
        
        else:
            print("You lose! Com wins 😢")
            break
        
    elif sum(user_deck) > 21:
        print("You lose!")
        
            
    
    