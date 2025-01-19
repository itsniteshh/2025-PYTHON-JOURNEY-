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
print(game[com_guess])

#user_input and assigning guess
#user_guess = int(input("Enter your guess:\n1 for rock, 2 for paper, 3 for scissors\n"))-1
user_guess = int(input("Enter your guess:\n1 for rock, 2 for paper, 3 for scissors\n"))-1
if user_guess > 0 and user_guess <=3:
    print(f"You chose: {game[user_guess]}")


#game logic
if user_guess == com_guess:
    print(f"Same hand used")
elif user_guess > 3 or user_guess <0:
    print("Invalid number")
elif user_guess == 0 and com_guess == 2:
    print("You win")
elif com_guess == 0 and user_guess == 2:
    print("You Lose")
elif com_guess > user_guess:
    print("You lose!")
elif user_guess > com_guess:
    print("You win!")
