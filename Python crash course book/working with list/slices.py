animals = ["lion", "dragon", "griffin", "pegasus", "Unicorn"]

print(f"The first 3 animals are: ")
for animal in animals[:3]:
    print(animal)
    
print("The last 3 animals are: ")
for animal in animals[-3:]:
    print(animal)
    
new_animal = animals[:]
print(new_animal)

new_animal.remove("griffin")
new_animal.append("dog")

print(new_animal)