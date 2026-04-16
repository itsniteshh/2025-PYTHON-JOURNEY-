"""
# Use for, split and if to create a steement to print words starting with s
st = "Print only the words that start with s in this sentence".lower()

for word in st.split():
    if word[0] == "s":
        print(word)

# using range to print all even nums from 0 to 10
for nums in range(0, 10):
    if nums % 2 == 0:
        print(nums

# List comprehension divisible by 3
by_3 = [nums for nums in range(1, 50) if nums % 3 == 0]
print(by_3))

# even words
st = "Print every word in this sentence that has an even number of letters"
for words in st.split():
    if len(words) % 2 == 0:
        print(words)

#fizzbuzz
for words in range(1, 100):
    if words % 15 == 0:
        print("FizzBuzz")
    elif words % 3 == 0:
        print("Fizz")
    elif words % 5 == 0:
        print("Buzz")
    else:
        print(words)"""

#list comprehension
st = "Create a list of the first letters of every word in this string"
new_words = [words[0] for words in st.split()]
"""
new_words = []
for words in st.split():
    new_words.append(words[0])"""

print(new_words)