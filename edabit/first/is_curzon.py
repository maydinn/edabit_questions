def is_curzon(num):
    """
    a function that returns True if num is a Curzon number, or False otherwise.
    If 1 plus 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a Curzon number.
    """
    return (2 ** num + 1) % (2 * num + 1) == 0


print(is_curzon(5))
