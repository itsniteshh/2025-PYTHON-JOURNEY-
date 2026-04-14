
# Brief about Data Types

# Numbers - Numbers are classified into INT and Float (also known as Decimals). When you divide something even if it's divides cleanly, it gets transformed into a decimal.
# Strings - Strings are everything under double or single string. Strings are mutable and they have lots of functions associated with them.
# Lists - Lists are also mutable and unordered. They are under a square bracket. They have many functions associated with them as well and can have numbers, strings, or even dicts or sets together.
# Tuples - Immutable and Unordered. They cannot be changed. They are under circular bracket
# Dict - They are under curly brackets and have key value pair in them.

# Numbers

"""print(4* (6 + 5)) # 44
print((4 * 6 + 5)) # 29
print((4 + 6 * 5)) # 34

print(type(3 + 1.5 + 4)) # 8.5 and type is float

# square root
print(89// 9)

#square
print(7*7)

# strings
s = "hello"
print(s[1])

print(s[::-1])

print(s[-1])
print(s[4])
"""
#list

"""
list1 = []
list1.append(0)
list1.append(0)
list1.append(0)
print(list1)

list1.insert(0, 0)
list1.insert(0, 0)
list1.insert(0, 0)
print(list1)

list3 = [1, 2, [3, 4, "hello"]]
list3[2][2] = "goodbye"
print(list3)

list4 = [5, 4, 3, 6, 1]
print(sorted(list4))

#Dictionaries

d = {"simple_key": "hello"}
print(d["simple_key"])

d = {"k1": {"k2": "hello"}}
print(d["k1"]["k2"])

d = {"k1": [{"nest_key": ["this is deep", ["hello"]]}]}
print(d["k1"][0]["nest_key"][1][0])

d = {"k1": [1, 2, {"k2": ["this is tricky", {"tough": [1, 2, ["hello"]]}]}]}
print(d["k1"][2]["k2"][1]["tough"][2][0])

# we cannot sort a dictionary because it contains values in key, values pair
"""

# Tuples cannot be changed or replaced but list on the other hand are mutable.
# to create a tuple we use circular brackets

# Sets
# sets are unique value list hence it cannot store duplicates.


