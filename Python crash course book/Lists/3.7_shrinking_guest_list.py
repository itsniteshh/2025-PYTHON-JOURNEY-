person = ["Lord shiva", "Nikola Tesla", "Elon Musk", "GOD", "Tutankhamen"]

person.insert(0, "Galileo")
person.insert(2, "King Ashoka")
person.append("Simon")

print("Sorry everyone! but it looks like I can invite only 3 person from the above list")

print(f"Sorry {person.pop(0)}, I can't invite you to dinner")
print(f"Sorry {person.pop(1)}, I can't invite you to dinner")
print(f"Sorry {person.pop(-1)}, I can't invite you to dinner")
print(f"Sorry {person.pop(-1)}, I can't invite you to dinner")
print(f"Sorry {person.pop(2)}, I can't invite you to dinner")
print(person)

print(f"You are invited to my dinner party, {person[0]}")
print(f"You are invited to my dinner party, {person[1]}")
print(f"You are invited to my dinner party, {person[2]}")

del person [0]
del person [0]
del person [0]
print(person)