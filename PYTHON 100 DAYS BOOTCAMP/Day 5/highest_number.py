student_score = [150, 22, 192, 42, 42, 593, 22]

highest = 0

for num in student_score:
    if num > highest:
        highest = num
    else:
        pass
    
print(f"The highest score is {highest}")