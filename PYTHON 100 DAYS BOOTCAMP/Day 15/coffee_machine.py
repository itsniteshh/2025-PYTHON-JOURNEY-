from items import MENU, resources

#TODO: 3 - Show report of current resources
def current_report(MENU, RESOURCES):
    """printing report when the user asks for it"""
    
    Wat = resources["water"]
    Mi = resources["milk"]
    Coff = resources["coffee"]
    Mon = resources["money"]
    return Wat, Mi, Coff, Mon

#TODO: 4 - Check if resources are sufficient
def resources_sufficient(want, menu, water, milk, coffee, resources, Money):
    """to check if the resources are sufficient to make the drink"""
    if want == "espresso":
        if menu["espresso"]["ingredients"]["water"] <= water and menu["espresso"]["ingredients"]["coffee"] <= coffee:
            water -= menu["espresso"]["ingredients"]["water"]
            coffee -= menu["espresso"]["ingredients"]["coffee"]
            Money -= resources["money"]
        else:
            if menu["espresso"]["ingredients"]["water"] > water:
                print("Sorry! there is not enough water.")
                return False
            else:
                print("Sorry! there is not enough coffee")
                return False
            
    elif want == "latte":
        if menu["latte"]["ingredients"]["water"] <= water and menu["latte"]["ingredients"]["coffee"] <= coffee and menu["latte"]["ingredients"]["milk"] <= milk:
            water -= menu["latte"]["ingredients"]["water"] 
            coffee -= menu["latte"]["ingredients"]["coffee"] 
            milk -= menu["latte"]["ingredients"]["milk"] 
            Money -= resources["money"]
        else:
            if menu["latte"]["ingredients"]["water"] > water:
                print("Sorry! there is not enough water.")
                return False
            elif menu["latte"]["ingredients"]["coffee"] > coffee:
                print("Sorry! there is not enough coffee.")
                return False
            else:
                print("Sorry! there is not enough Milk.")
                return False
            
    elif want == "cappuccino":
        if menu["cappuccino"]["ingredients"]["water"] <= water and menu["cappuccino"]["ingredients"]["coffee"] <= coffee and menu["cappuccino"]["ingredients"]["milk"] <= milk:
            water -= menu["cappuccino"]["ingredients"]["water"]
            milk -= menu["cappuccino"]["ingredients"]["milk"]
            coffee -= menu["cappuccino"]["ingredients"]["coffee"]
            Money -= resources["money"]
        else:
            if menu["cappuccino"]["ingredients"]["water"] > water:
                print("Sorry! there is not enough water.")
                return False
            elif menu["cappuccino"]["ingredients"]["coffee"] > coffee:
                print("Sorry! there is not enough coffee.")
                return False
            else:
                print("Sorry! there is not enough Milk.")
                return False
    
    return True
            
#TODO: 5 - Process money
def process_money(MENU, resources, hundreds, fifties, tens, fives):
    input_total = 0
    
    

#TODO:6 - CHECK IF THE TRANSACTION IS SUCCESSFUL
def transaction_successful():
    pass

#TODO:7 - Make Coffee
game_running = True

while game_running:
    #TODO: 1 - USER PROMPT
    want = input("What would you like? (espresso/latte/cappuccino)").lower()

#TODO: 2 - DISABLING THE MACHINE IF THE COMMAND SAYS OFF
    if want == "off":
        game_running = False
    elif want == "report":
        Water, Milk, Coffee, Money = current_report(MENU, resources)
        print(f" Water: {Water}\n Milk: {Milk}\n Coffee: {Coffee}\n Money: {Money}")
    else:
        
        print("Please insert coins")
        hundreds = int(input("How many 100s?: "))
        fifties = int(input("How many 50s?: "))
        tens = int(input("How many 10s?: "))
        fives = int(input("How many 5s?: "))
        
        if want == "latte":
            check = resources_sufficient(want, MENU, Water, Milk, Coffee, resources, Money)
            if check:
                pass
        elif want == "espresso":
            check = resources_sufficient(want, MENU, Water, Milk, Coffee, resources, Money)
            if check:
                pass
        elif want == "cappuccino":
            check = resources_sufficient(want, MENU, Water, Milk, Coffee, resources, Money)
            if check:
                pass