#!/usr/bin/python3
def is_prime(number):
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            is_prime = False
    return is_prime

