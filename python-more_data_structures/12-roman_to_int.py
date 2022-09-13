#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not roman_string):
        return 0
    if (type(roman_string) != str):
        return 0
    # "ro_ab" stands for "roman to arabic"
    ro_ab = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }
    namor = roman_string[::-1]
    ac = 0
    for i in range(len(namor)):
        if (i < len(namor) - 1):
            if (ro_ab[namor[i]] > ro_ab[namor[i + 1]]):
                ac -= 2 * ro_ab[namor[i + 1]]
        ac += ro_ab[namor[i]]
    return ac
