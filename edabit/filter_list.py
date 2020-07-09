def filter_list(l):
    return list(filter(lambda x: type(x) == int, l))


print(filter_list([1, 2, 3, "a", "b", 4]))
