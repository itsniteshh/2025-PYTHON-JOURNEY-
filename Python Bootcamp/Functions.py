# Warmup section
"""
#Leser of two evans - Given a function, return the lesser of two if both are even, return the greater if one or both are odd
def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 ==0:
        return min (a, b)
    else:
        return max (a, b)

print(lesser_of_two_evens(2, 1))

# Animal cracker - write a function that takes 2 word strings and return True if both words begin with same letter

def animal_cracker(text):
    new = text.split()
    
    return new[1][0] == new[0][0]

print(animal_cracker("Levelheaded Mlama"))"""

# Other side of seven - Given a value, return a value that is twice as far away on the other side of 7

def other_side_of_seven(num):
    distance = abs(7 - num)
    twice = distance * 2

    if num > 7:
        new_num = 7 - twice
    else:
        new_num = 7 + twice
    
    return new_num

print(other_side_of_seven(4))