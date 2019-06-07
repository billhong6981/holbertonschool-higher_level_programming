#!/usr/bin/python3
"""my module"""


def number_of_lines(filename=""):
    """my function"""
    n = 0
    with open(filename) as f:
        for line in f.read():
            if line == '\n':
                n += 1
    f.close()
    return n
