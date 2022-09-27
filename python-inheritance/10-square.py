#!/usr/bin/python3
"""modules that defines a class regarding a geometry"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class representing a rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2
