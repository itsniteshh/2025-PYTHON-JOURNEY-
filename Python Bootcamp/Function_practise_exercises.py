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
"""

# Level 2 problems

def laughter(pattern, text):
    #counts the number of times a given pattern appears in a string, including overlap
    new_text = []
    new_pattern =[]
    counter = 0

    for t in text:
        for p in pattern:
            if text[t] == pattern[p]:
                counter += 1



    return counter

print(laughter("hah", "hahahah"))
