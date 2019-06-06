#!/usr/bin/python3
"""my module"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """my rectangle class"""

    def __init__(self, width, height):
        """instantiation function"""
        self.__width = width
        self.__height = height
        super().__init__()
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
