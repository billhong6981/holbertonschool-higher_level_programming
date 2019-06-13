#!/usr/bin/python3
"""my class module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """my Square class module"""

    def __init__(self, size, x=0, y=0, id=None):
        """instance of class constructor"""
        super().__init__(size, size, x, y, id)
        self.size = self.width

    def __str__(self):
        """return a string for print function"""
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """private instance attribute size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """private instance attribute size setter"""
        self.width = value

    def update(self, *args, **kwargs):
        """assigns attributes function"""
        if not args and not kwargs:
            return
        if args:
            ar_list = ["id", "size", "x", "y"]
            for i, ar in enumerate(args):
                setattr(self, ar_list[i], ar)
        else:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)

    def to_dictionary(self):
        """return the square dictionary"""
        dic = super().to_dictionary()
        dic["size"] = dic["width"]
        del dic["width"]
        del dic["height"]
        return dic
