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

print(animal_cracker("Levelheaded Mlama"))

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

# Level 1 problems

# OLD MACDONALD: write a function that capitalizes the first and fourth letters of a name
def old_macdonald(name):
    first = name[0:3].title()
    fourth = name[3:].title()
    return first + fourth

print(old_macdonald("macdonald"))

# almost there - given an integer, return True if n is within 10 of either 100 or 200
def almost_there(n):
    return abs(n - 100) <= 10 or abs(n - 200) <= 10

print(almost_there(209))

#LEVEL 2 Problems

# laughter - write a function that counts the number of times a given pattern appears in a string, including overlap
def laughter(pattern, text):
    pass

print(laughter("hah", "hahahah"))

# Paper doll - given a string, return a string where for every character in the original there are three char

def paper_doll(text):
    new_text = ""
    for t in text:
        new_text += t * 3
    return new_text

print(paper_doll("Nitesh"))

# BLACKjack - given three int between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's a 11, reduce the total by 10. Finally if the sum even after above exceeds 21, reurn "BUST"
def blackjack(a, b, c):
    total = a + b + c

    if total <= 21:
        return total
    elif total > 21 and (a == 11 or b == 11 or c == 11):
        return total - 10
    else:
        return "BUST"
print(blackjack(5, 6, 7))

# summer of 69: return the sum of nums in the array, except ignore sections of nums starting with 6 and extending to next 9. return 0 for no numbs
def summer_69(arr):
    pass

print(summer_69([1, 3, 5]))

#Challenging problems

# spy game - write a function that takes in a list of ints and returns True if both contain 007 in order
def spy_game(nums):
    order = ""
    for n in nums:
        if n == 0 or n == 7:
            order += str(n)
        
    return order == "007" 
print(spy_game([1, 7, 2, 0, 4, 5, 0]))

# count prime - function that returns the number of prime number, that exist up to and including a given num

def count_prime(num):
    pass

print(count_prime(100))

# master yoda - given a sentence, return the sentence with words reversed
def master_yoda(n):
    text = n.split()
    new = text[::-1]
    return " ".join(new)

print(master_yoda("I am home"))"""