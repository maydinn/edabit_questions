import datetime


def time_for_milk_and_cookies(date):
    """
    function that accepts a Date object and returns True if it's Christmas Eve (December 24th) and False otherwise.
    """
    return date.strftime("%B") == "December" and date.strftime("%d") == "24"
