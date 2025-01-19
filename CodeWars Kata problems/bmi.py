def bmi(weight, height):
    "a kata problem to calculate bmi of our boyd"
    bmi = weight / (height * height)
    
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25:
        return "Normal"
    elif bmi <= 30:
        return "Overweight"
    else:
        return "Obese"

