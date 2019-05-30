#!/usr/bin/python3
def magic_string(a="Holberton, "):
    setattr(magic_string, "i", getattr(magic_string, "i", 0) + 1)
    return (a*magic_string.i)[0:len((a*magic_string.i)) - 2]
