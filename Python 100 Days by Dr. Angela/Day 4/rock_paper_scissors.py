# rock wins against scissors
# scissors wins against paper
# paper wins against rock
import random

game = ["Rock", "Paper", "Scissors"] #Game

#User guess
user = int(input("Enter your guess? Type 1 for Rock, 2 for Paper and 3 for scissors\n"))-1
user_guess = game[user]
print(f"User chose: {user_guess}")

# Com guess
com = random.choice(game)
print(f"Com chose: {com}")

#game check

if user_guess == com:
    print("Match drawn")

elif user_guess == "Rock" and com == "Scissors":
    print("User wins!")

elif user_guess == "Scissors" and com == "paper":
    print("User wins")
    
elif user_guess == "Paper" and com == "Rock":
    print("User wins")

else:
    print("You lose! Com wins. ")