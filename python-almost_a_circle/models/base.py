#!/usr/bin/python3
"""module defining basic class"""
import json


class Base:
    """class with an instance counter"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns a string representation of a list of dicts"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        lst = []
        for i in list_objs:
            d = i.to_dictionary()
            lst.append(d)
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            f.write(cls.to_json_string(lst))
