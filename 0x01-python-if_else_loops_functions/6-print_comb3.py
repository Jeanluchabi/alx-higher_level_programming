#!/usr/bin/python3
for n in range(9):
    for m in range(n + 1, 10):
        if n * 10 + m < 89:
            print("{:d}{:d}".format(n,m), end=", ")
print("{:d}".format(89))
