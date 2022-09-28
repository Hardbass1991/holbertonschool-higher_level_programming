#!/usr/bin/python3
"""module that defines a class"""


class Student:
    """class representing a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        attrs_valid = True
        if attrs is None or type(attrs) != list:
            attrs_valid = False
        else:
            for attr in attrs:
                if type(attr) != str:
                    attrs_valid = False
                    break
        if attrs_valid:
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        if json:
            self.__dict__ = json
