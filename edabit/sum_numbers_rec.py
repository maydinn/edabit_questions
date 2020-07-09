def sum_numbers(n):
    """
    a function that calculates sum of from 1 to given number by using recursion
    """
    if n <= 1:
        return n
    return n + sum_numbers(n - 1)


print(sum_numbers(5))