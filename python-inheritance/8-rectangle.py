#!/usr/bin/python3
"""Class BaseGeometry"""


class BaseGeometry:
    """one mehtod"""
    def area(self):
        """public instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """base class Rectangle inherits from BaseGeometry"""


    def __init__(self, width, height):
        """Constructor method"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
