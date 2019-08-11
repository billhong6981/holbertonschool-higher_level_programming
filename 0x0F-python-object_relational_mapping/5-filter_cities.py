#!/usr/bin/python3
"""This script that lists content of states"""
import MySQLdb
from sys import argv


def list_states():
    """my function that lists states start with N"""
    kwargs = {
        "host": "localhost",
        "user": argv[1],
        "passwd": argv[2],
        "db": argv[3]
        }
    db = MySQLdb.connect(**kwargs)
    db = db.cursor()
    db.execute("""SELECT cities.name FROM cities
    JOIN states ON state_id=states.id WHERE states.name=%s
    ORDER BY cities.id""", (argv[4],))
    z = db.fetchall()
    s = ""
    for i in z:
        i = i[0] + ", "
        s += i
    print(s[:-2])

if __name__ == '__main__':
    list_states()
