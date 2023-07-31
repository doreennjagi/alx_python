#!/usr/bin/python3
def raise_exception():
    try:
        
        raise TypeError
    except TypeError as te:
        # Print the error message
        print("Exception raised")