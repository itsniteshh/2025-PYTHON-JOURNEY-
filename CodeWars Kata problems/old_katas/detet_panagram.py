def is_pangram(s):
    def is_true(s):
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
        count = 0
        for letters in s.lower():
            if letters not in alphabet:
                pass
            elif letters in alphabet:
                count += 1
                if count == 26:
                    return True
    if is_true(s):
        return True
    else:
        return False
        
        