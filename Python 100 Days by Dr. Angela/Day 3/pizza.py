print("Welcome to the Python pizza delivery")

size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want extra papperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0


if size == "S":
    bill += 15

elif size == "M":
    bill += 20
  
else:
    bill += 25
    
        
if size == "S" and pepperoni == "Y":
    bill += 2
else:
    bill += 3

if extra_cheese == "Y":
    bill += 1
    

print(f"Your total bill is {bill}")