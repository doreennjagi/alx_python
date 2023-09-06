#!usr/bin/python3
""" defines a class rectangle"""
class BaseGeometry:
    """initialise a class"""
    def area(self):
        """ the function raise an exception message"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """the function validate the interger value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """ defince the rectngle basegeometry"""
    def __init__(self, width, height):
        """ initialises the rectangle class attributes """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
