#!/usr/bin/python3
""" defines a square"""


class Square:
    """Square with size"""
    def __init__(self, size=0):
        """constructor of square object."""
    @property
    def size(self):
        """Getter for size"""
        return self.__size
    @size.setter
    def size(self, value):
        """setter for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an intenger")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the area of the square"""
        return self.__size ** 2
