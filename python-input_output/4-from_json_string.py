#!/usr/bin/python3
"""module that gets object from JSON string"""
import json


def from_json_string(my_str):
    """function that returns object from JSON string"""
    return json.loads(my_str)
