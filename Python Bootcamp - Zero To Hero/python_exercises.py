#  Warm up section

#Lesser of two evens - Write a fucntion that returns the lesser of two given numbers if both are eve4n, but returns the greater if one or both are odd

def lesser_of_two_evens(num1, num2):
    """do something"""
    
    if num1 % 2 == 0 and num2 % 2 == 0:
        if num1 > num2:
            return num2
        else:
            return num1
        
    else:
        if num1 > num2:
            return num1
        else:
            return num2

result = lesser_of_two_evens(23, 4)


# Animal cracker - write a function that takes a two word string and returns True if both begin with the same letter

def animal_cracker(text):
    
    t = text.split()
    return t[0][0] == t[1][0] 

animals = animal_cracker ("Levelheaded klama")


# The other sides of seven - Given a value, return a value that is twice as far away on the other side of 7

def other_side_of_seven(num):
    
    distance_from_seven = 7 - num
    twice = distance_from_seven * 2
    final =  7 + twice
    return final

seven = other_side_of_seven(12)

# Level 1 Problems

# Write a function that capitalizes the first and fourth letters of a name

def old_macdonald(name):
    n = []
    
    for w in name:
        n += w
  
    first = n[0].upper()
    fourth = n[3].upper()
    
    return f"{first}{name[1:3]}{fourth}{name[4:]}"
    
mac = old_macdonald("macdonald")


 # Master Yoda = Given a sentence, return a sentence with the words reversed

def master_yoda(text):
    l = text.split()
    l = l[::-1]
    
    t = ""
    for la in l:
        t += la
        t+= " "
        
    return t

master = master_yoda("I am home")


# Almost there = Given an integer n, return True if n is within 10 of either 100 or 200

def almost_there(num):
    
    within_hun = abs(num - 100)
    within_two = abs(num - 200)
    
    return within_hun <= 10 or within_two <=10
    
    
num = almost_there(192)


# Level 2 problems

# Laughter - write a function that counts the numbver of times a given pattern appears in a string, including overlap



# Paper doll - given a strintg, reutn a string where every character in the orig8inal there are three characters

def paperdoll(text):
    
    new = ""
    for words in text:
        new += words * 3
        
    return new

paper = paperdoll("Hello")

# Blackjack - given 3 integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their

def blackjack (a, b, c):
    
    total = a + b + c
    
    if total > 21 and ((a == 11) or (b == 11) or (c == 11)):
        total -= 10
    
    if total <= 21:
        return total
    
    else:
        return "BUST"

black = blackjack(5, 6, 7)


# Summer of 69: Return the sum of the numbers in the array, expcept ignore sections of numbers starting with a 6 and ending to the next 9 (every 6 will be followed by at least one 9.) Return 0 for no numbers

def summer_69(arr):
    order = [6, 9]
    
    
summer = summer_69([1, 3, 5])


#Challenging problems

#spy game - write a function that takes in a list of integers and returns True if it contains 007 in order
"""
def spy_game(nums):
    
    order = "007"
    new = []
    
    for n in nums:
        if n == 0:
            new += n
        
        elif n == 7:
            new += n
    
    return f"{new[0]}{new[1]}{new[2]}" == "007"

spy = spy_game([1, 2, 3, 4, 0, 0, 7, 5])
"""
new = [1, 2, 4, 5]
ne = ""

for n in new:
    ne.append(n)
    
print(ne)