#!/usr/bin/python3
"""my class module"""


class Student:
    """my class"""

    def __init__(self, first_name, last_name, age):
        """instantial function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """get the obj attributes dictionary function"""
        dict = {}
        if hasattr(self, "__dict__"):
            if attrs is None:
                return getattr(self, "__dict__")
            if type(attrs) is list and all(type(s) is str for s in attrs):
                ls = [s for s in attrs if s in self.__dict__]
                for i in ls:
                    dict[i] = self.__dict__[i]
                return dict
            return getattr(self, "__dict__")
