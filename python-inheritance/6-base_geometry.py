#!/usr/bin/python3
"""modules that defines a class regarding a geometry"""


class BaseGeometry:
    """class about geometry"""
    def area(self):
        raise Exception("area() is not implemented")
