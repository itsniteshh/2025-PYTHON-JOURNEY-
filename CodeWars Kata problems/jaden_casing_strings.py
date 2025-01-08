def to_jaden_case(string):
    
    global output
    output = ""
    
    new_str = string.split()
    for words in new_str:
        output += words.capitalize() + " "
    final = output.rstrip()
    return final