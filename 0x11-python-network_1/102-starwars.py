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
        a = dic["results"]
        if dic:
            print("Number of results:", dic["count"])
            while dic["next"] is not None:
                req = requests.get(dic["next"])
                dic = req.json()
                a += dic["results"]
            for i in a:
                print(i["name"])
                for j in i["films"]:
                    film = requests.get(j)
                    print('\t{}'.format(film.json().get('title')))
        else:
            print("No result")
    except:
        pass
