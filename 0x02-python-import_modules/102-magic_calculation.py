#!/usr/bin/python3
def magic_cslculation(a, b):
    try:
        from magic_calculation_102 import add, sub
    except ImportError:
        print("Error: Unable to import required functions.")
        return None

    if a < b:
        result = add(a, b)
        for n in range(4, 6):
            result = add(result, n)
        return result
    else:
        return sub(a, b)
