def round_to_next5(n):
    import math
    if n < 0 and n > -5:
        return 0
    elif n % 5 == 0:
        return n
    elif n % 5 < 0:
        return 5
    else:
        counter = math.floor(n / 5 )
        return (counter + 1) * 5