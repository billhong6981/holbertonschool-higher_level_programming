#!/usr/bin/python3
"""a rectangle module"""


class Rectangle:
    """a Rectangle class"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initializes instance method"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """private instance variable getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """private instance variable setter"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        "private instance variable getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """private instance variable setter"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """gets rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """returns perimeter of rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return ((self.width + self.height) * 2)

    def rectangel_string(self):
        """returns a string"""
        string = ""
        if self.width == 0 or self.height == 0:
            return
        string = ('#' * self.width + '\n') * self.height
        string = string[0:len(string) - 1]
        return string

    def __str__(self):
        """returns a string for print"""
        return self.rectangel_string()

    def __repr__(self):
        """returns a string of code"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """del instance"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
