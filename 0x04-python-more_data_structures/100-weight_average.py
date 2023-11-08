#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    number = 0
    denu = 0

    for tu in my_list:
        number += tu[0] * tu[1]
        denu += tu[1]

    return (number / denu)

