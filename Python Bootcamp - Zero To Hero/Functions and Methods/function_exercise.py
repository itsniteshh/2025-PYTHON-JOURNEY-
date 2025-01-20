# WARMUP SECTION
'''
def lesser_of_two_evens(a, b):
    """to print lesser of two nums if both are even, but return greater if both or one is odd"""
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)
print(lesser_of_two_evens(24, 22))

def animal_cracker(text):
    """takes a two word string and returns True if both word begins with same letter"""
    new_word = text.find(" ")+1
    return text[0] == text[new_word]
print(animal_cracker("Levelheaded lama"))

def makes_twenty(n1, n2):
    """given two integers, return True if sum of them is 20 or if one of them is 20, else Return False"""
    return n1 + n2 >= 20 or (n1 == 20 or n2 == 20)
print(makes_twenty(9, 10))

# Level 1 problems

def old_macdonald(name):
    """capitalizes the first and fourth letters of a name"""
    front = name[:3].capitalize()
    mid = name[3].upper()
    last = name[4:]
    return front + mid + last
print(old_macdonald("macdonald"))

def master_yoda(text):
    """returns the sentence with words reversed"""
    new_text = text.split()
    return " ".join(new_text[::-1])
print(master_yoda("Home, the place where I belong"))

def almost_there(n):
    """returns true if n is within 10 of either 100 or 200"""
    return abs(100- n) <= 10 or abs(200 - n) <= 10
print(almost_there(180))
'''
# Level 2