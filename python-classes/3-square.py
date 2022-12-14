#!/usr/bin/python3
"""Module defining a square
"""


class Square:
    """A square
    """
    def __init__(self, s=0):
        """Initialization of square

        Args:
            size (int): Size of square
        """
        self.__size = s

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, val):
        if type(val) != int:
            raise TypeError("size must be an integer")
        elif val < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = val

    def area(self):
        return self.__size ** 2
