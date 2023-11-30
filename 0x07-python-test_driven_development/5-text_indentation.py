#!/usr/bin/python3
"""Function to print 2 new lines after each ., ? and : in a text"""


def text_indentation(text):
    """Function to indent text."""

    if type(text) is not str:
        raise TypeError("text must be a string")

    for x in text:
        print(x, end='')
        if x == '.' or x == '?' or x == ':':
            print("\n")
