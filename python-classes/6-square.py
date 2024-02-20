#!/usr/bin/python3
""" defines a square"""


class Square:
    """Square with size"""
    def __init__(self, size=0, position=(0, 0)):
        """constructor of square object."""
        self.size = size
        self.position = position
    
    def area(self):
        return self.__size ** 2
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
    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        if len(value) != 2 or type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(value[0], int) and isinstance(value[1], int):
            if value[0] >= 0 and value[1] >= 0:
                self.__position = (value[0], value[1])
            else:
                raise TypeError("position must be a tuple of 2 " + "positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
    
    def my_print(self):
        """prints in stdout the square with #"""
        if self.__size > 0:
            if self.__position[1] > 0:
               print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
        else:
                print()
