#!/usr/bin/python3
"""module that writes a JSON string to a file"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes a JSON string to a file"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
