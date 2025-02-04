guests = ["Tutankhamen", "Nicola Tesla", "Lord Shiva", "Galileo", "Stephen Hawking", "Gods", "Aliens"]

for names in guests:
    print(names)
    
guests.insert(0, "Shah rukh khan")
guests.append("First human being born")
guests.insert(4, "Lord Rama")
print("\n")
for names in guests:
    print(names)