#!/usr/bin/python3
"""my module"""


def class_to_json(obj):
    """my json obj function"""

    if hasattr(obj, "__dict__"):
        return getattr(obj, "__dict__")
