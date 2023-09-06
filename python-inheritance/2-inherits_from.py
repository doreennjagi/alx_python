#!usr/bin/python3
""" defines the object class"""
def inherits_from(obj, a_class):
    """ initialises the object is a subclass of a specified class"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
