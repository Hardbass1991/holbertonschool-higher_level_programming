#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    res = sorted(a_dictionary.items())
    for k, v in res:
        print(f"{k}: {v}")
