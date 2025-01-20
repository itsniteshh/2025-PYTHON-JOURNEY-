'''
def vol(r):
    """computes the volume of a sphere given its readius"""
    volume = 4/3 * 3.14 * (r ** 3)
    return volume
print(vol(2))

def ran_check(num, low, high):
    """checks whether a number is in a given range"""
    is_present = None
    for nums in range(low, high+1):
        if nums == num:
            is_present = True
            break
        else:
            is_present = False
    
    if is_present:
        return f"{num} is in the range of {low} and {high}"
    else:
        return f"{num} not in the range of {low} and {high}"
print(ran_check(10, 2, 7))

def up_low(s):
    """function that accepts a string and calculates the number of upper case
        letter and lower case letters"""
    upper_letters = 0
    lower_letters = 0
    
    for text in s:
        if text.isupper():
          upper_letters += 1
        elif text.islower():
            lower_letters += 1 
        else:
            pass
    return f"No. of Upper case characters: {upper_letters}\nNo. of Lower case characters: {lower_letters}"  
print(up_low("Hello Mr. Rogers, how are you this fine Tuesday?"))

def unique_list(lst):
    """takes a list and returns a new list with unique elements of the first list"""
    new_list = []
    
    for nums in lst:
        if nums in new_list:
            pass
        else:
            new_list.append(nums)
    return new_list
print(unique_list([1, 2, 2, 3, 4, 4, 5, 7, 7, 1, 2, 7]))
'''