#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            if i == len(row) - 1:
                # For the last element in the row, add a newline after the value
                print("{:d}".format(row[i]))
            else:
                # For other elements, add a space after the value
                print("{:d}".format(row[i]), end=" ")

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
