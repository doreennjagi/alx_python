# File: main.py

def main():
    a = 1
    b = 2

    # Import the add function from add_0.py
    from add_0 import add

    # Perform the addition and store the result in a variable
    result = add(a, b)

    # Print the result using string formatting
    print(f"{a} + {b} = {result}")

if __name__ == "__main__":
    main()
