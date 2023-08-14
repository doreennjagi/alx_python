#!usr/bin/python3
""" defines class rectangle"""
class BaseGeometry:
    """ intialise the class object"""
    def area(self):
        """ the function raises the exception message"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """ initialises the integer value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """ defines the rectangle class"""
    def __init__(self, width, height):
        """ initialises the class attributes"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    
    def area(self):
        """ initialises the area of the triangle"""
        return self.__width * self.__height
    
    def __str__(self):
        """ defines how the rectang;les should  be displayed when using the print function """
        return f"[Rectangle] {self.__width}/{self.__height}"
