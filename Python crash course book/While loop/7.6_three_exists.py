count = 0

while True:
    age = input("Enter your age: ")
    
    if age == "quit":
        break
    
    if int(age) < 3:
        print("Ticket is free for you, kiddo")
    elif int(age) < 12:
        print("Ticket price for you is 10")
    elif int(age) < 60:
        print("Ticket price for you is 15")
    
    count += 1
    print(count)