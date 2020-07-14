def factorial_rec(n):
    """
    a function that return factorial of given number by using recursion
    """
    if n <= 1:
        return n
    return n * fac(n - 1)


print(factorial_rec(5))
