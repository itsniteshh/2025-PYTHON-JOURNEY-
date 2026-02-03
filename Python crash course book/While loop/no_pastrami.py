sandwich_orders = ["toast", "pastrami", "cheese toast", "pastrami", "french toast", "pastrami", "veg"]

print("We have run of of pastrami")

while "pastrami" in sandwich_orders:
    making_sandwich = sandwich_orders.remove("pastrami")

print("\nWe have prepared the following sandwich:")
for sandwich in sandwich_orders:
    print(sandwich)