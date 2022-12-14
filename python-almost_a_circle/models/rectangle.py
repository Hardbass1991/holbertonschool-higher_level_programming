#!/usr/bin/python3
"""module that defines a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """rectangle class, with attributes regarding size"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """method that returns the area of the instance rectangle"""
        return self.width * self.height

    def display(self):
        """method that prints out a representation of the rectangle"""
        if self.width == 0 or self.height == 0:
            print()
        else:
            for i in range(self.y):
                print()
            for i in range(self.height):
                for j in range(self.x):
                    print(" ", end='')
                for j in range(self.width):
                    print("#", end='')
                print()

    def update(self, *args, **kwargs):
        """method that updates instance attributes"""
        if not args:
            # print(self.__dict__)
            for k, v in kwargs.items():
                if "_Rectangle__" + k in self.__dict__.keys():
                    self.__dict__["_Rectangle__" + k] = v
                else:
                    self.__dict__[k] = v
        else:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                elif i == 4:
                    self.y = args[i]

    def to_dictionary(self):
        """method that prints a dictionary representation of object"""
        list_from_dict = list(self.__dict__.items())
        lst = []
        for i in list_from_dict:
            if i[0].startswith("_Rectangle__"):
                lst.append(i[0][12:])
            else:
                lst.append(i[0])
            lst.append(i[1])
        return {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
