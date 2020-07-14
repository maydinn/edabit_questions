def sort_by_length(lst):
    """
     a function that returns a list of strings sorted by length in ascending order.
    """
    return sorted(lst, key=len)


print(sort_by_length(["john", "max", "markus", "mustafa"]))
