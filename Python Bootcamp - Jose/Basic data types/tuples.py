name = ("Nitesh", "jha", "Nitesh")
print(type(name))

#name[0] = "Nitesh" # This will give an error because tuple is immutable

print(name.count("Nitesh"))
print(name.index("jha"))

mytup = tuple("Nitesh")
