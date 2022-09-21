#!/usr/bin/python3
"""Module defining a square
"""


class Square:
    """A square
    """
    def __init__(self, size=0):
        """Initialization of square

        Args:
            size (int): Size of square
        """
        self.size = size

    @property
    def size(self):
        """Returns public version of attribute"""
        return self.__size

    @size.setter
    def size(self, val):
        """Sets input attribute after validating"""
        if type(val) != int:
            raise TypeError("size must be an integer")
        if val < 0:
            raise ValueError("size must be >= 0")
        self.__size = val
