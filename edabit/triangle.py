def triangle(n):
    """
    function that gives the number of dots with its corresponding triangle number of the sequence.
    This Triangular Number Sequence is generated from a pattern of dots that form a triangle.
    The first 5 numbers of the sequence, or dots, are:
    1, 3, 6, 10, 15
    """
    return sum(range(1, n + 1))


print(triangle(6))
