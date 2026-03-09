def make_shirt(text, size = "L"):
    """a function that returns the size and message to be printed"""

    tsize = f"The size of the shirt is {size}"
    ttext = f"The message on the shirt should be {text}"

    return tsize, ttext

t_shirt, t_text = make_shirt("Let's do it")
print(t_shirt)
print(t_text)