#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_of_orders = list(a_dictionary.keys())
    list_of_orders.sort()
    for x in list_of_orders:
        print("{}: {}".format(x, a_dictionary.get(x)))

