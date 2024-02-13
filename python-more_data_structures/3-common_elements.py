#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_set = set()
    for i in set_1:
        for j in set_2:
            if j == i:
                common_set.add(j)
    return common_set
