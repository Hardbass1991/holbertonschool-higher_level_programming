#!/usr/bin/python3
"""module that loads a string as a JSON object"""
import json


def to_json_string(my_obj):
    """function that returns JSON representation of input object"""
    return json.dumps(my_obj)
