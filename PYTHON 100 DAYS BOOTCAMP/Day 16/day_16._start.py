from turtle import Turtle, Screen
"""
nit = Turtle()
nit.shape("turtle")
nit.color("blue")
my_screen = Screen()

print(my_screen.canvheight)
nit.forward(100)
nit.right(90)
nit.forward(100)
nit.right(90)
nit.forward(100)
nit.right(90)
nit.forward(100)
my_screen.exitonclick()
"""

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtel", "Charmender", "Bulbasaur"], "l")
table.add_column("Type", ["Electric Mouse", "Water", "Fire", "Grass"], "l")
print(table)



