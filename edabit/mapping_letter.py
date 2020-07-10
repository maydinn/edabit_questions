def mapping_letter(letters):
    """
    a function that creates a dictionary with each (key, value) pair being
    the (lower case, upper case) versions of a letter, respectively.
    """
    my_list = list(map(lambda x: x.upper(), letters))
    return dict(zip(letters, my_list))


print(mapping_letter(["a", "b", "c"]))


def mapping_letter(letters):
    my_list = list()
    for i in letters:
        my_list.append(i.upper())
    return dict(zip(letters, my_list))


print(mapping_letter(["a", "b", "c"]))


def mapping_letter(letters):
    return {item: item.upper() for item in letters}


print(mapping_letter(["a", "b", "c"]))