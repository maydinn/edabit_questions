def cars_needed(n):
    """
    A typical car can hold 4 passengers and 1 driver, overall allowing 5 people to travel around.
    Given n number of people, return how many cars are needed to seat everyone comfortably.
    """
    return (n // 5) + (1 * (n % 5 != 0))
