#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_directory = a_dictionary.copy()
    list_of_keys = list(new_directory.keys())

    for n in list_of_keys:
        new_directory[n] *= 2

    return new_directory

