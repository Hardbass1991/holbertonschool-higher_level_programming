#!/usr/bin/python3
"""Module featuring a function that tells whether an input object
is an instance of an input class"""


def is_same_class(obj, a_class):
    """function that returns whether obj is an instance of class a_class"""
    if type(obj) == a_class:
        return True
    return False
