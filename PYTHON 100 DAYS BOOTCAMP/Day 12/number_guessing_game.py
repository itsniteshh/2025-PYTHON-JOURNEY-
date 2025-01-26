from art import logo
import random

# Basic To-dos and random number
print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")
guess = random.randint(1, 100)
print(guess)

#TODO:1 - choosing the difficulty level
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "easy" or difficulty == "hard":
    pass
else:
    print("Invalid response. Please try again")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

#TODO:2 - counting the number of lives remaining
def counting_lives(difficulty):
    """to count the remaining attempt"""
    lives = 0
    
    if difficulty == "easy":
        lives = 10
    elif difficulty == "hard":
        lives = 5     
    return lives
remaining_lives = counting_lives(difficulty)

#TODO:3 - asking for guess till the user guesses sucessfully
end_of_game = True

while end_of_game:
    print(f"You have {remaining_lives} attempts left.")
    user_guess = int(input("Make a guess: "))
    
    if user_guess == guess:
        print(f"You have guessed the number correctly! You Win.")
        end_of_game = False
    elif user_guess > guess:
        print("Too high.")
        remaining_lives -= 1
    elif user_guess < guess:
        print("Too low.")
        remaining_lives -= 1
    
    if remaining_lives == 0:
        print("You are out of guesses. You Lose!")
        end_of_game = False