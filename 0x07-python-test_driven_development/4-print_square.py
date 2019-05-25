#!/usr/bin/python3
"""Prints Square
Args:
    size: a integer
"""


def print_square(size):
    """function prints square with # charater
    Return: None
    """

    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print('#'*size)
