def invert(lst):
    new = []
    
    for nums in lst:
        if len(lst) == 0:
            return lst
        elif nums > 0:
            new.append(-abs(nums))
        else:
            new.append(abs(nums))
    
    return new