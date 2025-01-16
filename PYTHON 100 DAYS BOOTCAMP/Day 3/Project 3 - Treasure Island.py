print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("You're at a cross road. Where do you want to go \n Type 'Left' or 'Right'\n").lower()
if direction == "left":
    lake = input("You've come to a lake. There is an island in the mimddle of the lake \n Type'wait' to wait for a boat or 'Swim'\n").lower()
    if lake == "swim":
        door = input("You arrive at an island. There is a big house with 3 doors. \n 'red', 'yellow' or 'blue' \n").lower()
        if door == "blue":
            print("Hurrah! You found the treasures with Gold! The One Piece is yours!")
        else:
            print("You were stuck in the fire from the door! You died! Game Over")
    else:
        print("You waited long enough! the land beneath you collapsed and you died! Game Over")
else:
    print(f"You failed. Monsters came out of the right direction! Game Over")

