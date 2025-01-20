word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
import random
from hangman_art import logo, stages

choosen_word = random.choice(word_list)
print(logo)

# TODO- 4 - making blanks the size of choosen_word
guessed_word = []
#display = ""

for _ in choosen_word:
    guessed_word += "_"
    
# TODO- 5 - running a while loop
end_of_game = True
lives = 6

while end_of_game:
    # TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter\n").lower()

    # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
    #  is, "Wrong" if it's not.
    
    for count, word in enumerate(choosen_word):
        if word == guess:
            guessed_word[count] = word
            display += word
    
    print(guessed_word)
    #print(display)
    if guess not in choosen_word:
        lives -= 1
        print(f"{guess} not in our guessed word")
        print(stages[lives])
        
        if lives == 0:
            print("You are out of guesses! You Lose")
            end_of_game = False
        
    elif "_" not in guessed_word:
        print(f"You have guessed all the letters in the word {choosen_word} correctly! You win!")
        end_of_game = False
    else:
        pass

