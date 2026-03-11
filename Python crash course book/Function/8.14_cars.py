def car(manufacturer, model_name, **Car_info):
    """a function to store car details"""

    Car_info["Manufacturer"] = manufacturer
    Car_info["Model Name"] = model_name

    return Car_info

c = car("BMW", "M340i", Price = "75L", Make = 2026)
print(c)