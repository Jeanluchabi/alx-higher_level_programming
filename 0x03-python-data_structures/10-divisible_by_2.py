#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    fresh_list = []
    for n in range(len(my_list)):
        if my_list[n] % 2 == 0:
            fresh_list.append(True)
        else:
            fresh_list.append(False)
    return fresh_list
