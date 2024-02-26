#!/usr/bin/python3
"""function that returns the dictionary
description with simple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object:"""


def class_to_json(obj):
    """function that returns the dictionary
    description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object:"""
    dictionary = {}
    if hasattr(obj, '__dict__'):
        for key, value in obj.__dict__.items():
            if not callable(value):
                dictionary[key] = value
    return dictionary
