#!usr/bin/python3
""" defines a basegeometry class"""
class BaseGeometry:
    """intialises a class"""
    def area(self):
        """ the function raises an exception """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """ the fuction validates the integer value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
