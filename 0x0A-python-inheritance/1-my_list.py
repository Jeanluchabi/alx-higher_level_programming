#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        new_sorted_list = sorted(self)
        print(new_sorted_list)
