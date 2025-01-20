#myfile = open("demo.txt")

"""
print(myfile.read())
print(myfile.seek(0))
print(myfile.read())
"""

#print(myfile.readlines())

with open("demo.txt", mode= "a") as myfile:
    myfile.write("\nN")
     
    
"""
with open("demo.txt", mode= "r") as myfile:
    f = myfile.readlines()
    print(f)  
    
with open("demo.txt", mode= "w") as myfile:
    myfile.write("This is a my few message")
    
with open("demo.txt", mode= "r") as myfile:
    n = myfile.readlines()
    print(n)

"""