#!/usr/bin/python3
"""This module defines an adding function



"""


def add_integer(a, b=98):
    """Adding function

    """
    s = ['a', 'b']
    ab = [a, b]
    for i in range(len(ab)):
        if type(ab[i]) not in [int, float]:
            raise TypeError(f"{s[i]} must be an integer")
        elif type(ab[i]) == float:
            ab[i] = int(float(ab[i]))
    return int(ab[0] + ab[1])
