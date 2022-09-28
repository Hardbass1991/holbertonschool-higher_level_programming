#!/usr/bin/python3
"""module that adds all arguments to a Python list, and then saves
them to a file"""
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    a = load_from_json_file("add_item.json")
except FileNotFoundError:
    a = []
b = list(argv)
b.pop(0)
a.extend(b)

save_to_json_file(a, "add_item.json")
