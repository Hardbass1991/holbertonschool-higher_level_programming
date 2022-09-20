#!/usr/bin/python3
"""Module featuring a function that prints string with modifications
"""


def text_indentation(text):
    """Function that prints input string with modifications

    Args:
        text: input string
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    for i in text:
        print(i, end='')
        if i in ('.', '?', ':'):
            print('\n')
