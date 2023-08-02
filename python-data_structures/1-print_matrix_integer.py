#!/usr/bin/python
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            for j in range(len(row[i])):
                print("{:d}".format(row[i][j]), end="empty")
                if j != (len(row[i]) - 1):
                # For other elements, add a space after the value
                    print("", end=" ")
                    print("")
                    