#!/usr/bin/python3
"""a class Student that defines a student"""


class Student:
    """defines the class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
 
    def to_json(self):
        dictionary = {}
        if hasattr(self, '__dict__'):
            for key, value in self.__dict__.items():
                if not callable(value):
                    dictionary[key] = value
        return dictionary
