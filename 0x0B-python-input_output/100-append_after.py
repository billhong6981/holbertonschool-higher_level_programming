#!/usr/bin/python3
"""my module"""


def append_after(filename="", search_string="", new_string=""):
    """my function"""
    if filename == "" or search_string == "" or new_string == "":
        return
    if type(search_string) is not str or type(new_string) is not str:
        return
    with open(filename, "r") as f:
        line = f.readlines()
        f.close()

    with open(filename, "w") as f:
        for c in line:
            if search_string in c:
                c += new_string
            f.write(c)
