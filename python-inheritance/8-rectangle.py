#!/usr/bin/python3
"""modules that defines a class regarding a geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """class representing a rectangle"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
