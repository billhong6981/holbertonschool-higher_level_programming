#!/usr/bin/python3
"""my module"""


def read_file(filename=""):
    """my read file function"""

    with open(filename) as f:
        for line in f.read():
            print(line, end='')
    f.close()
