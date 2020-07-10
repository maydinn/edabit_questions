def next_in_line(lst, num):
    """
     a function that takes a list and a number as arguments. Add the number to the end of the list,
     then remove the first element of the list. The function should then return the updated list.
    """
    if not lst:
        return "No list has been selected"
    else:
        lst.pop(0)
        lst.append(num)
        return lst


print(next_in_line([1, 2, 3, 4], 5))
