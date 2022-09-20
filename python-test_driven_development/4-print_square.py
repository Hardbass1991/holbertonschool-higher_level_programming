#!/usr/bin/python3
"""Module featuring a function that prints a square of input size
"""


def print_square(size):
    """Function that prints a square of input size

    Args:
        size: size of square to print
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
