#!/usr/bin/python3
"""a module requests http response"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    req = requests.get(url)
    if req.status_code >= 400:
        print('Error code:', req.status_code)
    else:
        print(req.text)
