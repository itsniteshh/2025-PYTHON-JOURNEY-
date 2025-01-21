def calculate_love_score(name1, name2):
    """checks love score between 2 names based on TRUE LOVE"""
    word1 = "TRUE"
    word2 = "LOVE"
    
    first_score = 0
    second_score = 0
    
    both_name = name1 + name2
    
    for words in both_name.upper():
        if words in word1:
            first_score += 1
        else:
            pass
    
    for word in both_name.upper():
        if word in word2:
            second_score += 1
    
    love_score = str(first_score) + str(second_score)   
    return int(love_score)

print(calculate_love_score("Nitesh Jha", "Prerna Madan"))    