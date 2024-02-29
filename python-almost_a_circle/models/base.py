#!/usr/bin/python3
"""Base class of all the rest of the classes
of this project"""


class Base:
    """Base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id is None:
            __nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
