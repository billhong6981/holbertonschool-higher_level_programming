#!/usr/bin/python3
"""my class module"""
import json
import os
import csv


class Base:
    """my Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json format string"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves a json string to file"""
        with open(cls.__name__ + ".json", "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                s = [item.to_dictionary() for item in list_objs]
                f.write(cls.to_json_string(s))

    @staticmethod
    def from_json_string(json_string):
        """json string to python object"""
        if json_string is None or not json_string or \
           type(json_string) is not str:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates dummy instance of class"""
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 2)
            dummy.update(**dictionary)
            return dummy
        if cls.__name__ is "Square":
            dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """returns all enstances of class"""
        ins = []
        filename = cls.__name__ + ".json"
        if not os.path.isfile(filename):
            return []
        with open(filename, "r") as f:
            s = cls.from_json_string(f.read())
        for item in s:
            ins.append(cls.create(**item))
        return ins

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saves to csv file format"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as f:
            if list_objs is None or type(list_objs) is not list \
               or not all(isinstance(item, Base) for item in list_objs):
                f.write("[]")
            if list_objs and any(isinstance(item, Base) for item in list_objs):
                values = [obj.to_dictionary() for obj in list_objs]
                if cls.__name__ == "Rectangle":
                    csv_fields = ["id", "width", "height", "x", "y"]
                else:
                    csv_fields = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=csv_fields)
                writer.writeheader()
                for value in values:
                    writer.writerow(value)

    @classmethod
    def load_from_file_csv(cls):
        """loads from csv file format"""
        filename = cls.__name__ + ".csv"
        ins = []
        if not os.path.isfile(filename):
            return []
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                dic = {key: int(value) for key, value in row.items()}
                ins.append(cls.create(**dic))
            return ins

    @staticmethod
    def reset():
        """Resets the instance of class to zero"""
        Base._Base__nb_objects = 0
