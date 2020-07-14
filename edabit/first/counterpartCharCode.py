def counterpart_char_code(char):
    """
     a function that takes a single character as an argument
     and returns the char code of its lowercased / uppercased counterpart.
    """
    return ord(char.swapcase())


print(counterpart_char_code("a"))
