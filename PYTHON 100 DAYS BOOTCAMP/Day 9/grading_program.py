student_score = {
   "Nitesh": 88,
   "Arjun": 53,
   "Aman": 98,
   "Nishit": 64 
}

for name, grades in student_score.items():
    if grades >= 91:
        print(f"{name} has Outstanding grades")
    elif grades >= 81:
        print(f"{name} Exceeds expectations")
    elif grades >= 71:
        print(f"{name} grades are Acceptable")
    else:
        print(f"{name} has Failed")
        
