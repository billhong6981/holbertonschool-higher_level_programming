#!/usr/bin/python3
"""Adds two integers
Args:
    a: a integer
    b: b integer
"""


def add_integer(a, b=98):
    """function makes addition of two integers
    Return: returns sum of two integers
    """

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError('a must be an integer')
    if type(b) is not int:
        raise TypeError('b must be an integer')
    return (a + b)
