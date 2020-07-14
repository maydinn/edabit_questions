def double_char(txt):
    """
     a function that takes a string and returns a string in which each character is repeated once.
    """
    word = ""
    for i in txt:
        word += 2 * i
    return word
