"""
try:
    number = 10
    print(number)

except ZeroDivisionError as ZE:
    print(ZE)

except ValueError as VE:
    print(VE)
"""

file = open("app.txt", "w")

file.write("Let's do it, 20206 is ours to conquer")
print(file)

file.close()