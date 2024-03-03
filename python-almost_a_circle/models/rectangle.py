#!/usr/bin/python3
"""
Module defining a class Rectangle that inherits from Base
"""


from models.base import Base


class Rectangle(Base):
    """
    Args:
        Base (_type_): _description_
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Returns:
            _type_: _description_
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the Rectangle
        """
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle
        with the character #
        """
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        return (
            "[Rectangle] ({}) {}/{} - {}/{}".format
            (self.id, self.x, self.y, self.width, self.height)
        )

    def update(self, *args, **kwargs):
        """Method that asign an argument to each attribute
        """
        Attr = ["id", "width", "height", "x", "y"]

        if args is not None and args != ():
            for i, value in enumerate(args):
                setattr(self, Attr[i], value)
        else:
            for key, value in kwargs.items():
                if key in Attr:
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of
        a rectangle
        """
        dict_rectangle = {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
        return dict_rectangle
