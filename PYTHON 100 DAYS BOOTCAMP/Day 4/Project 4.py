rock = '''
rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

# container for storing games
game = [rock, paper, scissors]

# assigning guess to computer
com_guess = random.randint(1, len(game))-1

#user_input and assigning guess
#user_guess = int(input("Enter your guess:\n1 for rock, 2 for paper, 3 for scissors\n"))-1
user_guess = game[int(input("Enter your guess:\n1 for rock, 2 for paper, 3 for scissors\n"))-1]
print(f"You chose: {user_guess}")
print(f"Com chose: {game[com_guess]}")

#game logic
if user_guess == com_guess:
    print(f"Same hand used")
elif user_guess == "rock" and com_guess == "scissors":
    print("You win")
elif user_guess == "scissors" and com_guess == "paper":
    print("You win")
elif user_guess == "paper" and com_guess == "rock":
    print("You win")
else:
    print("Com wins!")