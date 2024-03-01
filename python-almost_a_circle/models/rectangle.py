#!/usr/bin/python3
"""
class Rectangle that inherits from Base
"""


class Rectangle(Base):
    """
    Args:
        Base (_type_): _description_
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Args:
            width (_type_): _description_
            height (_type_): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        super()__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        @property
        def width(self):
            """getter for width"""
            return self.__width
        
        @width.setter
        def width(self, value):
            """setter for width"""
            self.__width = value
        
        @property
        def height(self):
            """Getter for height"""
            return self.__height
        
        @height.setter
        def height(self, value):
            """setter for height"""
            self.__width = value
        
        @property
        def x(self):
            """getter for x"""
            return self.__x
        
        @x.setter
        def x(self, value):
            """setter for x"""
            self.__x = value
        
        @property
        def y(self):
            """getter for y"""
            return self.__y
        
        @y.setter
        def y(self, value):
            """setter for y"""
            self.__y = value
