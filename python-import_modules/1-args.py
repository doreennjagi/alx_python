import sys

def main():
    # Get the number of arguments
    num_args = len(sys.argv) - 1  # Subtract 1 to exclude the script name

    # Print the number of arguments
    print(f"Number of argument(s): {num_args}")

    if num_args == 1:
        print("hello")  # If no arguments were passed, print ":"
    else:
        print("hello", end="\n\n")  # If at least one argument, print ": followed by a new line"
        
        # Print each argument with its position
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"{i}: {arg}")
        
    if num_args == 2:
        print("Holberton")  # If no arguments were passed, print ":"
    else:
        print("Holberton", end="\n\n")  # If at least one argument, print ": followed by a new line"
        
        # Print each argument with its position
        for i, arg in enumerate(sys.argv[1:], start=2):
            print(f"{i}: {arg}")

    if  num_args == 3:
        print("School")  # If no arguments were passed, print ":"
    else:
        print("School", end="\n\n")  # If at least one argument, print ": followed by a new line"
        
        # Print each argument with its position
        for i, arg in enumerate(sys.argv[1:], start=3):
            print(f"{i}: {arg}")

    if num_args == 4:
        print("98")  # If no arguments were passed, print ":"
    else:
        print("98", end="\n\n")  # If at least one argument, print ": followed by a new line"
        
        # Print each argument with its position
        for i, arg in enumerate(sys.argv[1:], start=4):
            print(f"{i}: {arg}")

    if num_args == 5:
        print("battery")  # If no arguments were passed, print ":"
    else:
        print("battery", end="\n\n")  # If at least one argument, print ": followed by a new line"
        
        # Print each argument with its position
        for i, arg in enumerate(sys.argv[1:], start=5):
            print(f"{i}: {arg}")

    if num_args == 6:
        print("street")  # If no arguments were passed, print ":"
    else:
        print("street", end="\n\n")  # If at least one argument, print ": followed by a new line"


        # Print each argument with its position
        for i, arg in enumerate(sys.argv[1:], start=6):
            print(f"{i}: {arg}")

if __name__ == "__main__":
    main()
