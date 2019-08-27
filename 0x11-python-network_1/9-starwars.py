#!/usr/bin/python3
"""a module requests http response"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) == 1:
        r2 = ""
    else:
        r2 = argv[1]
    url = "https://swapi.co/api/people/?search={}".format(r2)
    try:
        req = requests.get(url)
        dic = req.json()
        if dic:
            print("Number of results:", dic["count"])
            for i in dic["results"]:
                print(i["name"])
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
