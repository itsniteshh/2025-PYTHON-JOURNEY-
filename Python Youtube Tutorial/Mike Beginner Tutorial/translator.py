# Translator that translates vowerls into g

vowels = ["a", "e", "i", "o", "u"]

text = input("Enter the word to be translated: ")
translation = ""

for words in text:
    if words in vowels:
        translation += "g"
    else:
        translation += words

print(translation)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         