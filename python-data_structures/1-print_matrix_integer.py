#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
                # For other elements, add a space after the value
                print("{:d}".format(row[i]), end=" ")
                print(" ")