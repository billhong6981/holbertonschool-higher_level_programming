#!/usr/bin/python3
"""my module"""
import json


def load_from_json_file(filename):
    """my json str to python obj function"""
    with open(filename, "r") as f:
        py_obj = json.load(f)
    return py_obj
