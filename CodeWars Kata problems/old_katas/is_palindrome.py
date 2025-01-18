#print("HEllo world")

def is_palindrome(s):
    new_word = []
    for words in s.lower():
        new_word += words
    if new_word == new_word[::-1]:
        return True
    else:
        return False

