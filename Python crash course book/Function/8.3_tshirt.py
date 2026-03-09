def make_shirt(size, text):
    """a function that returns the size and message to be printed"""

    tsize = f"The size of the shirt is {size}"
    ttext = f"The message on the shirt should be {text}"

    return tsize, ttext

t_shirt, t_text = make_shirt("L", "Let's do it")
print(t_shirt)
print(t_text)