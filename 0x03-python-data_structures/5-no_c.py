#!/usr/bin/python3
def no_c(my_string):
    new_str = my_string.translate({ord(n): Nonefor n in 'cC'})
    return new_str
