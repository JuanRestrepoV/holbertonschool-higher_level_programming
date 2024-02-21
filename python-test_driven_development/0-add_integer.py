#!/usr/bin/python3
 """
    Adds two integers.

    Parameters:
    - a (int or float).
    - b (int or float).
    Raises:
    - TypeError: If a or b are not integers or floats.
    """
def add_integer(a, b=98):
    """
    Returns:
    - int: The addition of a and b as integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
