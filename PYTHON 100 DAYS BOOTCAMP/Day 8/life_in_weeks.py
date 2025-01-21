def life_in_weeks(age):
    """to check the remaining weeks we have left to live"""
    
    remaining_weeks = (90 - age) * 52
    
    return f"You have {remaining_weeks} weeks left."

print(life_in_weeks(40))