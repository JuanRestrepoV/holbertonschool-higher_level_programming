#!/usr/bin/python3
"""function that returns True if the object is exactly
an instance of the specified class"""


def is_same_class(obj, a_class):
    """Function that takes for arguments:
    -The object verified.
    -The class it is supossed to instance for.
    """
    return type(obj) is a_class
