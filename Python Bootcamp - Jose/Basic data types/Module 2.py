
"""
nums starting with s

st = 'Print only the words that start with s in this sentence'
for words in st.split():
    if words[0].lower() == "s":
        print(words)
        
"""
"""
even numbers with range fucntion

for words in range(0, 11):
    if words % 2 == 0:
        print(words)
"""

"""
List comprehension for divisible by 3

div3 = [nums for nums in range(1, 50) if nums % 3 == 0]
print(div3)
"""
"""
to print even if len is even and odd if len is odd

st = 'Print every word in this sentence that has an even number of letters'
for words in st.split():
    if len(words) % 2 == 0:
        print(f"{words} is even")
    else:
        print(f"{words} is odd")
"""
"""
fizzbuzz program

for nums in range(1, 100):
    if nums % 15 == 0:
        print(f"{nums} is FizzBuzz")
    elif nums % 3 == 0:
        print(f"{nums} is Fizz")
    elif nums % 5 == 0:
        print(f"{nums} is Buzz")
    else:
        print(nums)
"""

#fizzbuzz = [nums if nums % 15 == 0 elif for nums in range(1, 100)] - list comprehension fizzbuzz for later
"""
creating list with the first letter of every word in the string

st = 'Create a list of the first letters of every word in this string'
final_list = []
for nums in st.split():
    final_list += nums[0]
    
print(final_list)
"""

"""
List comprehension for the above code

st = 'Create a list of the first letters of every word in this string'
final_list = [nums[0] for nums in st.split()]
print(final_list)
"""