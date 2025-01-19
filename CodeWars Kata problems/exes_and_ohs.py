def xo(s):
    x_count = 0
    o_count = 0
    
    for digits in s.lower():
        if digits != "x" and digits != "o":
            return True
        elif (digits != "x" and digits == "o") or (digits != "o" and digits == "x"):
            return False
        elif digits == "x":
            x_count += 1
        elif digits == "o":
            o_count += 1
        
    return x_count == o_count

print(xo("oozz"))