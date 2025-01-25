from art import logo
print(logo)

#TODO:1 - getting the nums and operators
num1 = float(input("What's the first number?: "))

# TODO:2 - Write down the 4 caluclations
def calculation(n1, n2, operation):
    total = 0
    
    if operation == "+":
        total = n1 + n2
    elif operation == "-":
        total = n1 - n2
    elif operation == "*":
        total = n1 * n2
    elif operation == "/":
        total = n1 / n2
        
    return total

#TODO:3 - Making sure our program is running till the user says quit
end_of_game = True

while end_of_game:
    if another_try == "y":
        num1 = calculator
    elif another_try == "n":
        num1 = float(input("What's the first number?: "))
    else:
        end_of_game = False
        
        
    operator = input("\n+\n-\n*\n/\nPick an operator: ")
    if operator != "+" or operator != "-" or operator != "*" or operator != "/":
        end_of_game = False
        
    another_num = float(input("What's the next number?: "))
    calculator = calculation(num1,another_num, operator)
    print(calculator)
    
    another_try = input(f"Type 'Y' to continue calculating with {calculator}, or Type 'n' to start a new calc: ").lower()
    
    