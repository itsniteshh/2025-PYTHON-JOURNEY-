text = "I love Python"

#result = " ".join(word[::-1] for word in text.split())

words = text.split()
reversed_words = []

for word in words:
    reversed_words.append(word[::-1])

result = " ".join(reversed_words)
print(result)