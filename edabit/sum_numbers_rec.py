def sum_numbers(n):
    if n <= 1:
        return n
    return n + sum_numbers(n - 1)


print(sum_numbers(5))