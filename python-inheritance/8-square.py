#!usr/bin/ptyhon3
""" defines a square """
class BaseGeometry:
    """ initialise the object """
    def area(self):
        """ the function raises an exception """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """the function validate the interger value"""
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
        """ initialises the area of the rectangle"""
        return self.__width * self.__height
    
    def __str__(self):
        """ defines how the rectangles should  be displayed when using the print function """
        return f"[Rectangle] {self.__width}/{self.__height}"

class Square(Rectangle):
    """initialises the subclass object"""
    def __init__(self, size):
        """initialises the square attributes"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
    
    def __str__(self):
        """ defines how the square should  be displayed when using the print function """
        return f"[Square] {self.__size}/{self.__size}"
