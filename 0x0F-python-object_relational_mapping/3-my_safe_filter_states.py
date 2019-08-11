#!/usr/bin/python3
"""This script safe from SQL injection"""
import MySQLdb
from sys import argv


def list_states():
    """my function that lists states from user input"""
    kwargs = {
        "host": "localhost",
        "user": argv[1],
        "passwd": argv[2],
        "db": argv[3]
        }
    db = MySQLdb.connect(**kwargs)
    db = db.cursor()
    db.execute("""SELECT * FROM states WHERE name=%s ORDER BY id""", (argv[4],))
    z = db.fetchall()
    for i in z:
        print(i)

if __name__ == '__main__':
    list_states()
