#!/usr/bin/python3
def validate_password(password):
    # Check password length
    if len(password) < 8:
        return False

    # Check for at least one uppercase letter, one lowercase letter, and one digit
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)

    if not (has_uppercase and has_lowercase and has_digit):
        return False

    # Check for spaces
    if ' ' in password:
        return False

    # If all checks pass, return True
    return True

# Test cases
print(validate_password("Password123"))  # True
print(validate_password("Abcd123"))      # False (length < 8)
print(validate_password("ABC123"))       # False (missing lowercase letter)
print(validate_password("abcd123"))      # False (missing uppercase letter)
print(validate_password("Password 123")) # False (contains space)

