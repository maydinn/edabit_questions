def divisible_by_five(n):
    """
    a function that returns True if an integer is evenly divisible by 5, and False otherwise.
    """
    if n % 5 == 0:
        return True
    else:
        return False 


print(divisible_by_five(6))
