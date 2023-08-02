#!/usr/bin/python
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end="empty")
            if j != (len(matrix[i]) - 1):
                print("", end=" ")
                print("")
                    