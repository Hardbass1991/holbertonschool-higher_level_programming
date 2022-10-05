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
        """saves string representation to file"""
        lst = []
        for i in list_objs:
            d = i.to_dictionary()
            lst.append(d)
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(cls.to_json_string(lst))

    @staticmethod
    def from_json_string(json_string):
        """returns input string as list"""
        if not json_string or json_string is None:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates new instance with attributes from dictionary"""
        try:
            a = cls.size
            new = cls(1)
        except AttributeError:
            new = cls(1, 1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """loads list of dicts from file and returns list of objects"""
        lst = []
        file_exists = False
        with open(cls.__name__ + ".json", "r", encoding="utf-8") as f:
            file_exists = True
            dcts = cls.from_json_string(f.read())
            for dct in dcts:
                lst.append(cls.create(**dct))
        return lst
