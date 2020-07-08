def integer_boolean(n):
    """
     a function which returns a list of booleans, from a given number.
     Iterating through the number one digit at a time,
     append True if the digit is 1 and False if it is 0.
    """
    lst = list()
    for i in n:
        if i == "1":
            lst.append(True)
        else:
            lst.append(False)
    return lst


print(integer_boolean("1001000111"))
