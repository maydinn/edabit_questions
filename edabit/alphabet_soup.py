from functools import reduce


# first way
def alphabet_soup(txt):
    """
     a function that takes a string and returns a string with its letters in alphabetical order.
    """
    return reduce(lambda x, y: x + y, sorted(txt))


print(alphabet_soup("hello"))


# second way
def alphabet_soup(txt):
    word = ""
    for i in sorted(txt):
        word += i
    return word


print(alphabet_soup("hello"))
