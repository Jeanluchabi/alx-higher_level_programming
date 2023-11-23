#!/usr/bin/python3
import sys
from calculator_1 import add, subtract, multiply, divide

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)

    x = int(sys.argv[1])
    operator = sys.argv[2]
    y = int(sys.argv[3])

    if operator == '+':
        result = add(x, y)
    elif operator == '-':
        result = subtract(x, y)
    elif operator == '*':
        result = multiply(x, y)
    elif operator == '/':
        result = divide(x, y)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(x, operator, y, result))
    sys.exit(0)
