fav_places = {
    "nitesh": {
        "place": "Nepal"
    },
    
    "purnima": {
        "place": "Himachal"
    },
    
    "arjun": {
        "place": "lonavala"
    }
}

for k, v in fav_places.items():
    print(f"{k.title()} favourite place is:")
    print(f"{v["place"]}\n")