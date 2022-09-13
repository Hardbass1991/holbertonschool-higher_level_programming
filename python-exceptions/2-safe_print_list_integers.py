#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n = 0
    for i in range(x):
        try:
            if type(my_list[i]) == int:
                print(my_list[i], end='')
                n += 1
        except IndexError:
            break
    print()
    return n
