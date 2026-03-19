# WarmUp Section

""" Lesser of Two EVEns

def lesser_of_two_evens(a, b):
    #function to return the lesser of two given numbers if both are even, but returns the greater if one or both are odd

    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    
    else:
        return max(a, b)
    
print(lesser_of_two_evens(2, 4))


def animal_crackers(text):
    # takes a two word string and returns True if both begin with the same letter

    new_text = text.split()
    return new_text[0][0] == new_text[1][0]

print(animal_crackers("Crazy Cama"))

def other_side_of_seven(num):
    iven a value, return a value that is twice as far away on the other side of 7
    distance = abs(7 - num)
    twice = distance * 2

    if num > 7:
        new_num = 7 - twice
    else:
        new_num = 7 + twice
    
    return new_num

print(other_side_of_seven(4))

#Level 1 problems

def old_macdonald(name):
    #capitalizes the first and forth letters of a name

    first = name[0:3].capitalize()
    mid = name[3].capitalize()
    final = name[4:]

    return first + mid + final

print(old_macdonald("macdonald"))


def master_yoda(text):
    # given a sentence, reutn a sentence with the words reversed

    new = text.split()
    return " ".join(new[::-1])

print(master_yoda("I am home"))

from math import ceil
def almost_there(n):
    #given an integer n, return True if n is within 10 of either 100 or 200
    if n > 111:
        n = ceil(n / 2)

    return abs(n - 100) <= 10

print(almost_there(209))

# Level 2 problems

def laughter(pattern, text):
    #counts the number of times a given pattern appears in a string, including overlap
    counter = 0
    p_length = len(pattern)

    for t in range(len(text) - p_length + 1):
        if text[t: t + p_length] == pattern:
            counter += 1

    return counter
print(laughter("hah", "hahahah"))

def paper_doll(text):
    # given a string, return a string where for every character in the original there are three characters
    new_text = ""
    for t in text:
        new_text += t * 3
    
    return new_text
print(paper_doll("Hello"))


def blackjack(a, b, c):
    # given three integers between 1 and 11, if their sum if less than or equal to 21, return their sum. 
    # If their sum exceeds 21 and there's an eleven, reduce the sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return "BUST".
    total = a + b + c

    if a == 11 or b == 11 or c == 11:
        total -= 10
    
    if total <= 21:
        return total
    
    else:
        return "BUST"
    
print(blackjack(9, 9, 11))

def summer_69(arr):
    # return the sum of numbers in an array, except ignore sections of numbers starting with a 6
    # and extending to the next 9. Return 0 for no numbers
    add = True
    total = 0

    for nums in arr:
        while add:
            if nums != 6:
                total += nums
                break
            else:
                add = False
        while not add:
            if nums != 9:
                break
            else:
                add = True
                break

    return total
    
print(summer_69[1, 3, 5])

def has_33(nums):
    # returns True if the array contains a 3 next to a 3 somewhere
    
    for i in range (0, len(nums)-1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

print(has_33([1, 3, 3]))


# CHALLENGING PROBLEM

def spy_game(nums):
    # Takes a list of int and returns True if it contains 007 in order
    order = ""
    for n in nums:
        if n == 0:
            order += str(n)
        elif n == 7:
            order += str(n)

    return order == "007" 

print(spy_game([1, 7, 2, 0, 3, 4, 5, 0]))
"""


def count_primes(num):
    # returns the number of prime numbers that exist up to and inccluding a given number
    how 
    if num < 2:
        return 0
    
    primes = [2]

    while 
"""
# Extra Hard or just for fun

def print_big(letter):
    # takes a single letter and returns a 5x5 representation of that letter

    big = {
        "a": '    *  '
        '        *  *'
                        
    }
    """