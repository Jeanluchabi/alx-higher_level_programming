#!/usr/bin/python3
a = 10
b = 5

from calculator_1 import add, subtract, multiply, divide

result_ad = add(a, b)
result_sub = subtract(a, b)
result_mul = multiply(a, b)
result_div = divide(a, b)

print(f"{a} + {b} = {result_ad}")
print(f"{a} - {b} = {result_sub}")
print(f"{a} * {b} = {result_mul}")
print(f"{a} / {b} = {result_div}")
