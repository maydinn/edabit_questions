def factorial(num):
    """
     a function that takes an integer and returns the factorial of that integer.
     That is, the integer multiplied by all positive lower integers.
    """
    if num == 0:
        return 1
    else:
        for i in range(1, num):
            num *= i
        return num 


print(factorial(6))
