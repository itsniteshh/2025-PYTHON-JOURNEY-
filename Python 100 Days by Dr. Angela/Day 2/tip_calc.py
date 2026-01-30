print("Welcome to the tip calculator program!")

bill = float(input("What was the total bill?\n "))
tip = int(input("How much tip would you like to give?\n"))
split = int(input("How many people to split the bill?\n"))

total_bill = bill + (bill * (tip /100))

print(f"Each person should pay: ${round(total_bill/split, 2)}.")