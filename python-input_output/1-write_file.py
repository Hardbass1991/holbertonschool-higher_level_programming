#!/usr/bin/python3
"""module that writes to a file"""


def write_file(filename="", text=""):
    """function that writes to a file"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    return len(text)
