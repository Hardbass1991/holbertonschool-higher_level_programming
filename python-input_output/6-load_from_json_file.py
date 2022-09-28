#!/usr/bin/python3
"""module that creates an object from a JSON file"""
import json


def load_from_json_file(filename):
    """function that creates an object from a JSON file"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f.read())
