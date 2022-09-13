#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    common = list(filter(lambda x: x in set_2, set_1))
    not_common_1 = list(filter(lambda x: x not in common, set_1))
    not_common_2 = list(filter(lambda x: x not in common, set_2))
    return set(not_common_1 + not_common_2)
