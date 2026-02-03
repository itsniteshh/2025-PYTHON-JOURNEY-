vacation = {}
poll_active = True

while poll_active:
    
    name = input("Enter your name: ")
    destination = input("Enter your dream destination: ")
    
    vacation[name] = destination
    
    another_round = input("someone else wants to try? ")
    if another_round == "no":
        poll_active = False
    
    

for n, d in vacation.items():
    print(f"{n}'s dream destination is {d}")