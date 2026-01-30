my_pizza = ["cheese garlic", "pepperoni", "margherita"]

frnd_pizza = my_pizza[:]

my_pizza.append("paneer chilli")
frnd_pizza.append("mushroom")

print("My favourite pizzas are:")
for pizz in my_pizza:
    print(pizz)
    
print("\nMy friends fav pizza are: ")
for f in frnd_pizza:
    print(f)