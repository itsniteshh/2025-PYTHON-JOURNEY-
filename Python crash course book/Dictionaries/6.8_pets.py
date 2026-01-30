pet = {
    "dog": {
        "type": "pet dog",
        "owner": "nitesh"
    },
    
    "cat": {
        "type": "pet cat",
        "owner": "sameer"
    },
    
    "parrot": {
        "type": "bird",
        "owner": "shraddha"
    }
}

for k, v in pet.items():
    print(f"\nAnimal kingdomo: {k.title()}")
    
    print(f"animal type is: {v["type"].title()}")
    print(f"animal owner is: {v["owner"].title()}")