#!/usr/bin/python3
"""module that defines a function that checks whether the input object
belongs to input class, or a class that inherits from it"""


def is_kind_of_class(obj, a_class):
    """function that returns whether obj is an instance of a_class
    or of another class that inherits from it"""
    if type(obj) == a_class or a_class in type(obj).__bases__:
        return True
    return False
