#!/usr/bin/python3
"""my module"""
import json


def save_to_json_file(my_obj, filename):
    """my python obj to json file function"""
    with open(filename, "w") as f:
        s = json.dumps(my_obj)
        f.write(s)
