#!/usr/bin/python3
def magic_cslculation(a, b):
    from magic_calculation_102 import add, subtract
    if a < b:
        c = add(a, b)
        for n in range(4, 6):
            c = add(c, n)
        return c
    else:
        return (subtract(a, b))
