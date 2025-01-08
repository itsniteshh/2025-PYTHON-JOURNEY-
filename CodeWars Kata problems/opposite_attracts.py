def lovefunc( flower1, flower2 ):
    # a function which returns true if both num are diff(i.e. odd and even) or returns false if both are same (i.e. odd and odd and even and )
    if flower1 % 2 == 0 and flower2 % 2 != 0:
        return True
    elif flower2 % 2 == 0 and flower1 % 2 != 0:
        return True
    else:
        return False