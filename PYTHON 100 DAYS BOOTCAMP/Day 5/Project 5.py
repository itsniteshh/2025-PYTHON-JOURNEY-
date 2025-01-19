letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


import random
password = "" #a string for our final password

# random letters
for l in range(0, nr_letters):
    l = random.choice(letters)
    password += l

# random symbols
for s in range(0, nr_symbols):
    s = random.choice(symbols)
    password += s
 
# random numbers   
for n in range(0, nr_numbers):
    n = random.choice(numbers)
    password += n
    
print(f"Here is your simple password: {password}")

# advanced password
adv_password = [] #container for storing passwords
for p in password:
    adv_password += p 

random.shuffle(adv_password) #randomly shuffly the passwords

new_password = "".join(adv_password)
print(f"Here is your hard password: {new_password}")