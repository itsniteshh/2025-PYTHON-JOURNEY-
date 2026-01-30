fav_number = {
    "nitesh": 7,
    "ganesh": 10,
    "arjun": [7, 8],
    "prathmesh": [5, 2, 20],
    "aman": 9
}

for k, v in fav_number.items():
    print(f"\n{k.title()}'s favourite number is:")
    print(v)