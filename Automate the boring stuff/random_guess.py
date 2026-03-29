import random

guess = random.randint(1, 20)
print(guess)
print("I am thinking of a number between 1 and 20")

while True:

    user_guess = int(input("Take a guess: "))

    if guess > user_guess:
        print("Your guess is too low")

    elif guess < user_guess:
        print("Your guess is too high.")

    else:
        print("Good job! You guessed the word correctly!")
        break