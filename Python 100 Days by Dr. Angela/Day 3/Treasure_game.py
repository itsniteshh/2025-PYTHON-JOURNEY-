print("Welcome to the Treasure Island\nYour mission is to find the treasure.")

direction = input("You're at a cross road. Where do you want to go? Type Left or Right\n").lower()

if direction == "left":
    
    lake = input("You've come to a lake. There is an island in the middle of the lake. Type Wait to wait for a boat or Swim to Swim across\n").lower()    
    
    if lake == "wait":
        
        door = input("You arrive a the island unharmed. There are 3 doors in your front. Red, Yellow and Blue. Whic color do you choose?\n").lower()       
        
        if door == "red":
            
            print("Congrats! You found the 10M treasure chese")
        
        else:
            print("Game over! You fell into a pool of fire")
    
    else:
        print("Game over! A group of sharks ate you.")



else:
    print("Game Over! You were jumped by a group of tiger")
