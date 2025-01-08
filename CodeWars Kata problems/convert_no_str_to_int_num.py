def digitize(n):
    new_no = []
    final = []
    num = str(n)
    for numbers in num:
        new_no.append(numbers)
    old_num = new_no[::-1]
    
    for words in old_num:
        alpha = int(words)
        final.append(alpha)
    return final