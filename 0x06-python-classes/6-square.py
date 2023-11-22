#!/usr/bin/python3
"""Defines class Square"""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new square class

        Args:
            size (int): The size of a new square
            position (tuple): The position of a new square as a tuple (int, int)
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set the current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/set the current position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) for i in value) or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with a # character"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)


if __name__ == "__main__":
    my_square = Square(3, (1, 20))
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.position = (2, 3)
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()

    print("--")

