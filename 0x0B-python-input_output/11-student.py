#!/usr/bin/python3
"""my class module"""


class Student:
    """my class"""

    def __init__(self, first_name, last_name, age):
        """instantial function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """get the obj attributes dictionary function"""
        if hasattr(self, "__dict__"):
            return getattr(self, "__dict__")
