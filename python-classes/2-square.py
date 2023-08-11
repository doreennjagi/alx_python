#!/usr/bin/python3
""" defines a square"""
class mysquare:
    """ class square that defines a square"""
    def __init__(self, size=0):
        """ initializes square size of square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
mysquare = mysquare(5)
print("Area of square:", mysquare.area())
