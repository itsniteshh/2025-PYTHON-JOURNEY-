weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi <= 18.5:
    print("Underweight")
elif bmi <25:
    print("normal weight")
else:
    print("Overweight")