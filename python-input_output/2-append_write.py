#!/usr/bin/python3
"""function taht appends a string
at the end of a text file"""


def append_write(filename="", text=""):
    """returns the number of characters added"""
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
