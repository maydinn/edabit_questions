def filter_list(l):
    """
    a function that takes a list and return a list that includes just int values
    """
    return list(filter(lambda x: type(x) == int, l))


print(filter_list([1, 2, 3, "a", "b", 4]))
