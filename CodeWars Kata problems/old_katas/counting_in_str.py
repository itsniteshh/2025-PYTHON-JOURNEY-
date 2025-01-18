def str_count(strng, letter):
    count = 0
    
    for items in strng:
        if items == letter:
            count += 1
    
    return count