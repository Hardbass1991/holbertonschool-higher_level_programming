#!/usr/bin/python3
"""Module featuring a function that returns the list of attributes
of an object"""


def lookup(obj):
    """Function returns a list of the attributes of an input object"""
    return dir(obj)
