#!/usr/bin/python3
"""my module"""


class MyInt(int):
    """my class"""

    def __eq__(self, other):
        """duder special function"""
        if super().__eq__(self):
            return False

    def __ne__(self, other):
        """duder special function"""
        if super().__eq__(self):
            return True
