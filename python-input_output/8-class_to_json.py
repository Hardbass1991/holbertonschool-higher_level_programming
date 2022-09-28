#!/usr/bin/python3
"""module that returns dict of a class"""


def class_to_json(obj):
    """function that returns dict of a class"""
    return obj.__dict__
