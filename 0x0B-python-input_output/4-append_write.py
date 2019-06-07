#!/usr/bin/python3
"""my module"""


def append_write(filename="", text=""):
    """my append mode function"""
    with open(filename, "a+") as f:
        n = f.write(text)
    f.close()
    return n
