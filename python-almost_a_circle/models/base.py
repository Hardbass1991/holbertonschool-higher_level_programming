#!/usr/bin/python3
"""module defining basic class"""

class Base:
    """class with an instance counter"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
