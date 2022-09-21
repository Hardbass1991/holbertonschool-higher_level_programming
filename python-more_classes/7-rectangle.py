#!/usr/bin/python3
"""Module that defines a class Rectangle
"""


class Rectangle:
    """Rectangle class

    Attributes:
        height (int): height of rectangle
        width (int): width of rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Args:
            width (int): aforementioned width
            height (int): aforementioned height
        """
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    def __str__(self):
        """Prints a rectangle of matching height and width, using '#' """
        s = ""
        for i in range(self.__height):
            for j in range(self.__width):
                s += str(self.print_symbol)
            if i < self.__height - 1 and self.__height * self.__width > 0:
                s += "\n"
        return s

    def __repr__(self):
        """Return a repr string"""
        w = str(self.__width)
        h = str(self.__height)
        return "Rectangle(" + w + ", " + h + ")"

    def __del__(self):
        """Prints a farewell message on deletion"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

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

    def area(self):
        """Computes area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Computes perimeter of rectangle.
        If either width or height are 0, returns 0
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)
