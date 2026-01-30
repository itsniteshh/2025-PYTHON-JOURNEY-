# Write a bried about the following data strctures

# Numbers - They are classified into two types: Int and float.. Int is for integers value and Float is for decimal values
# Strings - anything and everything which comes under double or single quotes
# Lists - Lists are mutable objects in python. They go in set of brackets.
# Tuples - Tuples are immutable objects. They go in round brackets. Tuples cannot be replaced or modified
# Dict - key value pair objects in python. They are mutable.


# Numbers
print(4 * (6 + 5))
print( 4 * 6 + 5)
print( 4 + 6 * 5)

print(3 + 1.5 + 4)  #8.5 - Type float

# square roots 
print(25 /5) # we will use forward slash to check for square roots
print(5**2)

# Strings
# Given the string hello give an index command that returns e. Enter the code below

s = "hello"
print(s[1]) # printing e

print(s[::-1]) #string reversing using slicing

print(s[4:]) #method 1 using indexing

print(s[-1]) #method 2 using negative indexing


# Lists

list1 = [0, 0, 0] #method 1 of building list
list2 = [] #method 2 of building a list from scratch
list2.append(0)
list2.append(0)
list2.append(0)

list3 = [1, 2, [3, 4, "hello"]]
print(list3[-1][-1])

list4 = [5, 3, 4, 6, 2]
print(sorted(list4)) #method 1

list4.sort() #method 2
print(list4)


# Dictionaries

d = {"simple_key": "hello"}
new_d = d["simple_key"] #grabbing hello

d = {"k2": [{"nest_key": ["this is deep", ["hello"]]}]}
print(d["k2"][0]["nest_key"][1][0])

d = {"k1": { "k2" : "hello"}}
print(d["k1"]["k2"])

d = {"k1": [1, 2, {"k2": ["this is tricky", {"tough": [1, 2, ["hello"]]}]}]}
print(d["k1"][2]["k2"][1]["tough"][2][0]) #getting hello as output

# No, we cannot sort a dictionary because they are mutable and have key values pair



# Tuples 
# Tupes are immutable, Lists are mutable.
# we can create a tuple by passing a closing bracket or by using tuple function



# Sets
# sets are data types which have unique values in them. They don't have duplicates and can be sorted or replaced.

list5 = [1, 2, 2, 3, 3, 4, 5, 5, 4, 5, 7]
newset = set(list5)
print(newset)



# booleans
