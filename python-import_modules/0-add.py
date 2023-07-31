#!/usr/bin/python3
if __name__ == '__main__':
    from add_0 import add

a = 1
b = 2

def main():
    result = add(a, b)

    # Print the result using string formatting
    print("{} + {} = {}".format (a,b,result))


