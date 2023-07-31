def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        print("Inside result: {}".format(result))
    return result

# Test the function
result1 = safe_print_division(10, 2)   # Valid division
result2 = safe_print_division(12,2)    # Division by zero
result3 = safe_print_division(8, '2')  # Invalid division (TypeError)

print("Result 1:", result1)  # Output: Inside result: 5.0
print("Result 2:", result2)  # Output: Error: Division by zero. \n Inside result: None
print("Result 3:", result3)  # Output: Error: unsupported operand type(s) for /: 'int' and 'str' \n Inside result: None
