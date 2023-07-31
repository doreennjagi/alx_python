def raise_exception():
    try:
        # Raise a type exception with a custom message
        raise_exception(TypeError)
    except TypeError as te:
        # Print the error message
        print("Exception raised")

# Call the function to see the type exception in action
raise_exception()
