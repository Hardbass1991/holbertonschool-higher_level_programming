#!/usr/bin/python3
"""Module defining a square
"""


class Square:
    """A square
    """
    def __init__(self, s=0, p=(0, 0)):
        """Initialization of square

        Args:
            size (int): Size of square
        """
        self.__size = s
        self.__position = p

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, val):
        if type(val) != tuple or len(val) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(val[0]) != int or type(val[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if val[0] < 0 or val[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = val

    def area(self):
        return self.__size ** 2

    def my_print(self):
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end='')
            for j in range(self.__size):
                print("#", end='')
            print()
