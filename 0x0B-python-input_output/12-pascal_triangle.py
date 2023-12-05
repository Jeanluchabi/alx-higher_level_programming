#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tria = triangles[-1]
        temp = [1]
        for x in range(len(tria) - 1):
            temp.append(tria[x] + tria[x + 1])
        temp.append(1)
        triangles.append(tmp)
    return triangles
