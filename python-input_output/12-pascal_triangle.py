#!/usr/bin/python3
"""module that builds a matrix with a pascal triangle"""


def pascal_triangle(n):
    """function that returns a matrix with a pascal triangle of size n"""
    res = []
    if n <= 0:
        return res
    for i in range(n):
        row = []
        if i == 0:
            row.append(1)
            res.append(row)
        else:
            for j in range(i + 1):
                if (j - 1) >= 0:
                    left = res[i - 1][j - 1]
                else:
                    left = 0
                # print(f"i: {i}, j: {j}, left: {left}")
                try:
                    right = res[i - 1][j]
                except IndexError:
                    right = 0
                # print(f"i: {i}, j: {j}, right: {right}")
                row.append(left + right)
            res.append(row)
    return res
