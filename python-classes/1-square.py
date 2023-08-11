#!/usr/bin/python3
class mysquare:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("3")
        if size < 0:
            raise ValueError("3")
        self.__size = size

    def area(self):
        return self.__size ** 2
