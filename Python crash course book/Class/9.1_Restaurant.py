class Restaurant():
    """A class to show restaurant information"""

    def __init__ (self, name, cuisine_type):
        self.name = name
        self.cuisine = cuisine_type

    def describe_restro(self):
        """describes restaurants details"""
        print(f"Our Restaurant's name is {self.name}")
        print(f"Our Restaurant specializes in {self.cuisine}")

    def open_restaurant(self):
        """says wheter our restaurant is open or not"""
        print("Our Restaurant is open for dining today")


r1 = Restaurant("Nitesh", "chinese")
print(f"My restaurant's name is {r1.name}")
print(f"Our restaruant specializes in {r1.cuisine}")