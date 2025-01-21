# TODO-3: What happens if you try to shift z forwards by 9? Can you fix the code?
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#TODO - 5 Importing Logo for visibility
from art import logo

# TODO-1: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.
def caesar(direction, original_text, shift,):
    shifted_position = 0
    cipher_text = ""
    # TODO-3: What happens if you try to shift z forwards by 9? Can you fix the code?
    shifted_position = shifted_position % 26 # to make sure that shifted position is within len(alphabets) i.e 26
    
    for words in original_text.lower():
        if words in alphabet:
            word_position = alphabet.index(words)
            if direction == "encode":
                shifted_position = word_position + shift
            elif direction == "encode":
                shifted_position = word_position - shift
                
            shifted_position = shifted_position % 26
            cipher_text += alphabet[shifted_position]  
            
        else:
            cipher_text += words
                 
    return cipher_text

# TODO-2: Can you figure out a way to restart the cipher program?
end_of_game = True

while end_of_game:
    # TODO-4: What happens if the user enters a number/symbol/space?
    print(logo)
    text = input("Type your message:\n").lower()
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    shift = int(input("Type the shift number:\n"))   
    print(caesar(direction, text, shift))
    
    another_try = input("Do you want to send another cypher message?\n").lower()
    if another_try == "no":
        print(f"Thank you for using our Caesar Cipher game!")
        end_of_game = False