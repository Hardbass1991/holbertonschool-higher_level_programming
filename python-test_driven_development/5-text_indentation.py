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
    for i in range(len(text)):
        if not (i > 0 and text[i - 1] in ('.', '?', ':') and text[i] == ' '):
            print(text[i], end='')
        if text[i] in ('.', '?', ':'):
            print('\n')
