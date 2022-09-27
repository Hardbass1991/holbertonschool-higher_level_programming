#!/usr/bin/python3
"""module that defines a function that checks whether the input object
belongs to a class that inherits from the input class"""


def inherits_from(obj, a_class):
    """function that returns whether obj is an instance of a class that
    inherits from a_class"""
    if a_class in type(obj).__mro__ and a_class != type(obj):
        return True
    return False
