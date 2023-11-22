#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        printed_elements = 0
        for n in range(x):
            print(my_list[n], end="")
            printed_elements += 1
    except IndexError:
        pass
    finally:
        print()
        return printed_elements
