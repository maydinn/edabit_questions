def factorial(num):
    if num == 0:
        return 1
    else:
        for i in range(1, num):
            num *= i
        return num


print(factorial(6))