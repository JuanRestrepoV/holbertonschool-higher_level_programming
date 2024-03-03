#!/usr/bin/python3
"""
Module defining a class Square that inherits from Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square that inherits from Rectangle"

    Args:
        Rectangle (_type_): _description_
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return (
            "[Square] ({}) {}/{} - {}".format
            (self.id, self.x, self.y, self.width)
        )

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
