#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, subtract, multiply, divide
    
    a = 10
    b = 5

    result_add = add(a, b)
    result_sub = subtract(a, b)
    result_mul = multiply(a, b)
    result_div = divide(a, b)

    print("{} + {} = {}".format(a, b, result_add))
    print("{} - {} = {}".format(a, b, result_sub))
    print("{} * {} = {}".format(a, b, result_mul))
    print("{} / {} = {}".format(a, b, result_div))
