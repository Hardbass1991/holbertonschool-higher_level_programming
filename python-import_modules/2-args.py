#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    n = len(argv) - 1
    if (n == 0):
        print(f"{n} arguments.")
    elif (n == 1):
        print(f"{n} argument:")
    else:
        print(f"{n} arguments:")
    for i in range(1, n + 1):
        print(f"{i}: {argv[i]}")
