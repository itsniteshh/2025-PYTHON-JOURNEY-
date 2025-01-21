alphabet = [chr(i) for i in range(97, 123)]  # Creates ['a', 'b', ..., 'z']

def caesar(direction, original_text, shift):
    cipher_text = ""

    for char in original_text:
        if char in alphabet:
            old_position = alphabet.index(char)
            # Adjust shift direction
            new_position = (old_position + shift) if direction == "encode" else (old_position - shift)
            new_position %= 26  # Wrap around the alphabet
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char  # Keep non-alphabetic characters unchanged
    
    return cipher_text


end_of_game = True
while end_of_game:
    text = input("Type your message:\n").lower()
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction not in ["encode", "decode"]:
        print("Invalid direction. Please choose 'encode' or 'decode'.")
        continue

    shift = input("Type the shift number:\n")
    if not shift.isdigit():
        print("Please enter a valid number for the shift.")
        continue
    shift = int(shift)

    result = caesar(direction, text, shift)
    print(f"The resulting text is: {result}")
    
    another_try = input("Do you want to send another cipher message? Type 'yes' or 'no':\n").lower()
    if another_try == "no":
        print("Thank you for using our Caesar Cipher program!")
        end_of_game = False
