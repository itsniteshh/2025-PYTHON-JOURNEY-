from items import MENU, resources


#TODO: 1 - USER PROMPT
want = input("What would you like? (espresso/latte/cappuccino)").lower()

#TODO: 2 - DISABLING THE MACHINE IF THE COMMAND SAYS OFF
if want == "off":
    pass
elif want == "report":
    pass
    #(f"Water: {Water}\nMilk: {Milk}\nCoffee: {Coffee}\n Money: {Money}")

#TODO: 3 - Show report of current resources
def current_report(MENU, RESOURCES):
    """printing report when the user asks for it"""
    
    Wat = resources["water"]
    Mi = resources["milk"]
    Coff = resources["coffee"]
    return Wat, Mi, Coff

Water, Milk, Coffee = current_report(MENU, resources)

#TODO: 4 - Check if resources are sufficient
def resources_sufficient(want, menu, water, milk, coffee):
    """to check if the resources are sufficient to make the drink"""
    if want == "espresso":
        if menu["espresso"]["ingredients"]["water"] >= water and menu["espresso"]["ingredients"]["coffee"] >= coffee:
            water - menu["espresso"]["ingredients"]["water"]
            coffee - menu["espresso"]["ingredients"]["coffee"]
        else:
            if menu["espresso"]["ingredients"]["water"] < water:
                return "Sorry! there is not enough water."
            else:
                return "Sorry! there is not enough coffee"
            
    elif want == "latte":
        if menu["latte"]["ingredients"]["water"] >= water and menu["latte"]["ingredients"]["coffee"] >= coffee and menu["latte"]["ingredients"]["milk"] >= milk:
            water- menu["latte"]["ingredients"]["water"] 
            coffee -menu["latte"]["ingredients"]["coffee"] 
            milk - menu["latte"]["ingredients"]["milk"] 
        else:
            if menu["latte"]["ingredients"]["water"] < water:
                return "Sorry! there is not enough water."
            elif menu["latte"]["ingredients"]["coffee"] < coffee:
                return "Sorry! there is not enough coffee."
            else:
                return "Sorry! there is not enough milk"
            
    elif want == "cappuccino":
        if menu["cappuccino"]["ingredients"]["water"] >= water and menu["cappuccino"]["ingredients"]["coffee"] >= coffee and menu["cappuccino"]["ingredients"]["milk"] >= milk:
            water - menu["cappuccino"]["ingredients"]["water"]
            milk - menu["cappuccino"]["ingredients"]["milk"]
            coffee - menu["cappuccino"]["ingredients"]["coffee"]
        else:
            if menu["cappuccino"]["ingredients"]["water"] < water:
                return "Sorry! there is not enough water."
            elif menu["cappuccino"]["ingredients"]["coffee"] < coffee:
                return "Sorry! there is not enough coffee."
            else:
                return "Sorry! there is not enough milk"
            

    

#TODO: 5 - Process money
def process_money():
    pass

#TODO:6 - CHECK IF THE TRANSACTION IS SUCCESSFUL
def transaction_successful():
    pass

#TODO:7 - Make Coffeej
