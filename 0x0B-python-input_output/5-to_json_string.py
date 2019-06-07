#!/usr/bin/python3
"""my module"""
import json


def to_json_string(my_obj):
    """my write function using json module"""
    return json.dumps(my_obj, sort_keys=True)
