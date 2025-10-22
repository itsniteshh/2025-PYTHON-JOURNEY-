my_pizza = ["mushroom", "italiano", "crispy paneer", "chicken tandoori"]

friends_pizza = my_pizza[:]
print(friends_pizza)

my_pizza.append("garlic bread")
friends_pizza.append("veg tomato")

print(my_pizza)
print(friends_pizza)

print("\nI like the following pizz: ")
for m in my_pizza:
    print(m)
    
print("\nThis is what my friends like:")
for f in friends_pizza:
    print(f)