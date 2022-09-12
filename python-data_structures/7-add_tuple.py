#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tup = [0, 0]
    for i in range(2):
        if tuple_a:
            if i < len(tuple_a):
                tup[i] += tuple_a[i]
        if tuple_b:
            if i < len(tuple_b):
                tup[i] += tuple_b[i]
    return tup[0], tup[1]
