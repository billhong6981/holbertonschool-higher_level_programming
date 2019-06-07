#!/usr/bin/python3
"""my module"""


def write_file(filename="", text=""):
    """my write to file function"""
    with open(filename, "w+") as f:
        n = f.write(text)
    f.close()
    return n
