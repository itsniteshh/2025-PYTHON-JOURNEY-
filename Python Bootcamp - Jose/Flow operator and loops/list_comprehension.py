mylist = []

for letters in "mango":
    mylist.append(letters)

print(mylist)

new_list = [l for l in "apple"]
print(new_list)


myrange = [num ** 3 for num in range(10)]
print(myrange)

myrange = [num for num in range(10) if num % 2 == 0]
print(myrange)

myrange = [num if num % 2 != 0 else "ODD" for num in range(10) ]
print(myrange)