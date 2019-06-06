#!/usr/bin/python3
"""my module 1-my_list"""


class MyList(list):
    """class name MyList"""

    def __init__(self):
        """inherites parent class attributes"""
        super().__init__()

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
