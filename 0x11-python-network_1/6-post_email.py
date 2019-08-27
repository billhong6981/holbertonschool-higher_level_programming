#!/usr/bin/python3
"""a module requests http response"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    data = {'email': argv[2]}
    req = requests.post(url, data)
    print(req.text)
