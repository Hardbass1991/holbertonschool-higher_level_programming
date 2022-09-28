#!/usr/bin/python3
"""module featuring a functions that prints the contents of a .txt file"""


def read_file(filename=""):
    """function that prints the contents of a .txt file"""
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.read()
        print(lines, end='')
