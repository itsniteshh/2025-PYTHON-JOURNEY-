secret_word = "Purnima"
lives = 3

while lives != 0:
    user_guess = input("Enter your word guess: ")

    if user_guess == secret_word:
        print("Bingo! Your guess is correct!")
        break
    else:
        lives -= 1
        print("Your guess is incorrect!")

        if lives == 0:
            print("You lose")

    
