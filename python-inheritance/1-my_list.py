#!/usr/bin/python3
"""Module featuring a class that inherits from list"""


class MyList(list):
    """class that inherits from list"""
    def print_sorted(self):
        """method that prints sorted list"""
        print(sorted(self))
