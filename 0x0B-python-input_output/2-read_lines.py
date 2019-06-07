#!/usr/bin/python3
"""my module"""


def read_lines(filename="", nb_lines=0):
    """my read lines function"""
    n = 0
    with open(filename) as f:
        n = sum(1 for line in f)
        f.seek(0, 0)
        if nb_lines <= 0 or nb_lines >= n:
            for line in f:
                print(line, end='')
        else:
            for i in range(nb_lines):
                print(f.readline(), end='')
    f.close()
