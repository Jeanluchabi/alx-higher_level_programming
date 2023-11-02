#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    number_of_arguments = len(sys.argv)
    
    if number_of_arguments == 1:
        print("{} arguments.".format(number_of_arguments - 1))
    
    elif number_of_arguments == 2:
        print("{} arguments:".format(number_of_arguments - 1))

    else:
        print("{} arguments:".format(number_of_arguments -1))

    for x in range(1, number_of_arguments):
        print("{}: {}".format(x, sys.argv[x]))
