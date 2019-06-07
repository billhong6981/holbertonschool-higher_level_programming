#!/usr/bin/python3
"""my module"""
import sys
import os.path
from os import path
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


filename = "add_item.json"
obj = []
if path.isfile(filename):
    obj = load_from_json_file(filename)
save_to_json_file(obj + sys.argv[1:], filename)
