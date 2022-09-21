#!/usr/bin/python3
"""Module that defines a class Rectangle
"""


class Rectangle:
    """Rectangle class

    Attributes:
        height (int): height of rectangle
        width (int): width of rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Args:
            width (int): aforementioned width
            height (int): aforementioned height
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Returns public version of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets attribute value, handling exceptions

        Args:
            value (int): new value of width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns public version of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets attribute value, handling exceptions

        Args:
            value (int): new value of height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
