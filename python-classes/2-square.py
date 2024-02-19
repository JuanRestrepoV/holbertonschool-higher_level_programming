#!/usr/bin/python3
""" defines a square"""


class Square:
    """Square with size"""
    def __init__(self, size=0):
        """constructor of square object."""
        if not isinstance(size, int):
            raise TypeError("size must be an intenger")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
