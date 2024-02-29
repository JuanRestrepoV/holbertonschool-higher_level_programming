#!/usr/bin/python3
""" defines a square"""


class Square:
    """Square with size"""
    def __init__(self, size=0):
        """constructor of square object."""
        self.size = size
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
        return self.size ** 2
    def my_print(self):
        """prints in stdout the square with #"""
        if self.size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
