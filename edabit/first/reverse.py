def reverse(arg):
    """
      a function that reverses a boolean value and returns the string "boolean expected" if another variable type is given.
    """
    if type(arg) == bool:
        return not arg
    else:
        return "boolean expected"
