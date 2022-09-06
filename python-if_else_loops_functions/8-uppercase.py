#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if (i < len(str) - 1):
            a = ''
        else:
            a = '\n'
        if (97 <= ord(str[i]) <= 122):
            print("{:c}".format(ord(str[i]) - 32), end=a)
        else:
            print("{:c}".format(ord(str[i])), end=a)
