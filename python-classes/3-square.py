#!/usr/bin/python3
""" defines a square"""
class Square:
    """ class square that defines a square """
    def __init__(self, size=0): 
        """ initializes a square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size =size

    def area(self):
        """ return area"""
        return self.__size ** 2
    
