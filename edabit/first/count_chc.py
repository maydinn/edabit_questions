def count_characters(lst):
    """"
    a function that counts how many characters make up a rectangular shape. You will be given a list of strings.

    """
    word = ""
    for i in range(0, len(lst)):
        word += lst[i]
    return len(word)


print(count_characters([
    "###",
    "###",
    "###",
    "###"
]))
