#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newList = []
    for idx in my_list:
        newList.append(idx % 2 == 0)
    return newList
