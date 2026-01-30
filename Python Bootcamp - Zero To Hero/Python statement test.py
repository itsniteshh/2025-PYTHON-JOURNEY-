
# Use a for, .split and if to create a statement that will print out the word that starts with "s"
st = "Print only the words that start with s in this sentence"
for words in st.split():
    if words.startswith("s"): # or I could have used words[0]
        print(words)
        

# use range to print all the even numbers from 0 to 10

for nums in range(0, 10):
    if nums % 2 == 0:
        print(nums)

# using list comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

triplets = [num for num in range(1, 50) if num %  3 == 0]
print(triplets)

# Go through the string below and if the length of a word is even print "even"

st = "print every word in this sentence that has an even number of letters"
for words in st.split():
    if len(words) % 2 == 0:
        print(words)
        
# write a program that prints the integers from 1 to 100 but for multiples of three print "fizz" instead of the num, and for multiples fo five print "buzz". For numbers which are multiples of both three and 5 print "fizzbuzz"

for nums in range(0, 100):
    if nums % 3 == 0 and nums % 5 == 0:
        print("FizzBuzz")
    elif nums % 3 == 0:
        print("Fizz")
    elif nums % 5 == 0:
        print("Buzz")
    else:
        print(nums)
        
        
# use list comprehension to create a list of first letters of every word in the string below

st = "Create a list of the first letters of every word in this string"
new_st = []

for words in st.split():
    new_st += words[0]
print(new_st)

n_st = [words[0] for words in st.split()]
print(n_st)