# Translator that translates vowerls into g

vowels = ["a", "e", "i", "o", "u"]

text = input("Enter the word to be translated: ")

for words in text:
    if words in vowels:
        text[words] = "g"

print(text)