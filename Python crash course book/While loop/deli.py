sandwich_orders = ["toast", "cheese toast", "french toast", "veg", "cheese triple"]

finished_sandwich = []


while sandwich_orders:
    making_sandwich = sandwich_orders.pop()
    print(f"We are preparing your {making_sandwich}")
    
    finished_sandwich.append(making_sandwich)

print("\nWe have prepared the following sandwich:")
for sandwich in finished_sandwich:
    print(sandwich)