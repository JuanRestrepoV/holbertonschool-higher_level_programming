#!/usr/bin/python3
"""a class Student that defines a student"""


class Student:
    """defines the class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dictionary = {}
        if attrs is not None:
            for key, value in self.__dict__.items():
                if key in attrs:
                    dictionary[key] = value
            return dictionary
        return self.__dict__
