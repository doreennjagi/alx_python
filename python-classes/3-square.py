#!/usr/bin/python3
class square:
    def __init__(self, size=0):
        self.size = size
    def size(self):
        return self.__size
    def size(self, value):
        if type() is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
    
