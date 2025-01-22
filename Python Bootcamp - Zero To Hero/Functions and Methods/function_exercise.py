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
'''

# Level 1 problems
'''
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
'''
def has_33(nums): #this one is pending
    """given a list of ints, return TRUE if the array contains 3 next to a 3"""
    count = 0
    for n in nums:
        if n == 3:
            count += 1
print(has_33([1, 3, 3]))

def paper_doll(text):
    """return a string where for every character in the original there are 3 char"""
    final = ""
    for i in text:
        i *= 3
        final += i
    return final
print(paper_doll("Hello"))

def blackjack(a, b, c):
    """given 3 int between 1 and 11, if their sum is less than or equal to 21, return their sum.
        If their sum exceeds 21 and there's an 11, reduce the total sum by 10. Finally if sum even after
            adjustment exceeds 21, return BUST"""
    total = a+b+c
    
    if total <= 21:
        return total
    elif total >= 21 and (a == 11 or b == 11 or c == 11):
        total -= 10
        
        if total >= 21:
            return "BUST"
        else:
            return total
    else:
        return "BUST"
print(blackjack(9, 9, 11))
'''

# Hard level
def summer_69(arr): #incomplete
    """return the sum of nums, except ignore sections of numbers starting with a 6
        and extending to the next 9. (every 6 will definately be followed by a 9. Return 0 for no nums)"""
    if len(arr) == 0:
        return 0
print(summer_69([1, 3, 5]))