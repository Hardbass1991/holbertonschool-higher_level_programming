#!/usr/bin/python3
"""module defininf a Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """method that updates instance attributes"""
        if not args:
            # print(super().__dict__)
            for k, v in kwargs.items():
                if k == 'id':
                    self.__dict__[k] = v
                elif k == 'size':
                    self.__dict__["_Rectangle__width"] = v
                    self.__dict__["_Rectangle__height"] = v
                else:
                    self.__dict__["_Rectangle__" + k] = v
        else:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.size = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
