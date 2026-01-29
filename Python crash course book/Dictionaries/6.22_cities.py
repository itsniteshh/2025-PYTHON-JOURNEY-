cities = {
    "Mumbai": {
        "country": "India",
        "population": 35938539,
        "fact": "city of dreams"
    },
    
    "NewYork": {
        "country": "USA",
        "population": 57375563,
        "fact": "City of light"
    },
    
    "Real madrid": {
        "country": "Spain",
        "population": 587537,
        "fact": "city of football"
    }
}

for k, v in cities.items():
    print(f"\nName of the city: {k}")
    print(v["country"])
    print(v["population"])
    print(v["fact"])