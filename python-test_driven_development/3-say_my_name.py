#!/usr/bin/python3
"""Module featuring a function that prints input strings
"""


def say_my_name(first_name, last_name=""):
    """Function that prints input strings

    Args:
        first_name: first input string
        last_name: second input string
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
