from art import logo
import random
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def draw_card(cards):
    """Draws a single card from the deck."""
    return random.choice(cards)

def calculate_score(deck):
    """Calculates the total score of a given deck and handles Aces."""
    if sum(deck) == 21 and len(deck) == 2:
        return 0  # Represents a Blackjack
    
    if 11 in deck and sum(deck) > 21:
        deck.remove(11)
        deck.append(1)

    return sum(deck)

def compare_scores(user_score, computer_score):
    """Compares the user's and computer's scores and returns the result."""
    if user_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "Computer wins with a Blackjack!"
    elif user_score == 0:
        return "You win with a Blackjack!"
    elif user_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "Computer went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

def blackjack_game():
    """Main function to handle the Blackjack game."""
    clear_screen()
    print(logo)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    user_deck = [draw_card(cards), draw_card(cards)]
    computer_deck = [draw_card(cards), draw_card(cards)]

    game_over = False

    while not game_over:
        user_score = calculate_score(user_deck)
        computer_score = calculate_score(computer_deck)

        print(f"Your cards: {user_deck}, current score: {user_score}")
        print(f"Computer's first card: {computer_deck[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if another_card == 'y':
                user_deck.append(draw_card(cards))
            else:
                game_over = True

    # Computer's turn
    while computer_score != 0 and computer_score < 17:
        computer_deck.append(draw_card(cards))
        computer_score = calculate_score(computer_deck)

    print(f"Your final hand: {user_deck}, final score: {user_score}")
    print(f"Computer's final hand: {computer_deck}, final score: {computer_score}")
    print(compare_scores(user_score, computer_score))

# Start the game
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    blackjack_game()
