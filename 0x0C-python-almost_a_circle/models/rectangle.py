#!/usr/bin/python3
"""my class module"""
from models.base import Base


class Rectangle(Base):
    """my Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """private instance attribute getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """private instance attribute setter"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 1:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """private instance attribute getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """private instance attribute setter"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 1:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """private instance attribute getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """private instance attribute setter"""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """private instance attribute getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """private instance attribute setter"""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """area function"""
        return self.width * self.height

    def display(self):
        """display function"""
        print('\n'*self.y, end='')
        print(((' '*self.x + '#'*self.width + '\n')*self.height)[:-1])

    def __str__(self):
        """return the string for print"""
        return "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """update the update() function"""
        if not args and not kwargs:
            return
        if args:
            ar_list = ["id", "width", "height", "x", "y"]
            for i, ar in enumerate(args):
                setattr(self, ar_list[i], ar)
        else:
            self.id = kwargs.get('id', self.id)
            self.width = kwargs.get('width', self.width)
            self.height = kwargs.get('height', self.height)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)

    def to_dictionary(self):
        """returns the rectangle dictionary"""
        dic = {}
        for k, v in self.__dict__.items():
            if k[0] is '_':
                dic[k.split('__')[1]] = v
            else:
                dic[k] = v
        return dic
