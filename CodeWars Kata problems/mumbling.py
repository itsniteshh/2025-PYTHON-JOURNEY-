def accum(st):
    """accum('abcd') -> 'A-Bb-Ccc-Dddd'"""
    final = ""
    for counter, words in enumerate(st, start = 1):
        new = words * counter
        final += new.title()
        final += "-"
    
    return final[:-1]