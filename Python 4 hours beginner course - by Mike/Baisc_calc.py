
num1 = int(input("Enter the first number: "))
ops = input("Emter the execution you want to do: \n + for Addition, - For subtraction, * for Multiplication and / For Division: ")
num2 = int(input("Enter the second number: "))


if ops == "+":
    print( num1 + num2)

elif ops == "-":
    print(num1 - num2)

elif ops == "*":
    print( num1 * num2)

else:
    print(num1 / num2)