#!/usr/bin/python3
"""a class MyList that inherits from list"""


class MyList(list):
    """class Mylist"""
    def print_sorted(self):
        new_list = sorted(self)
        print(new_list)
