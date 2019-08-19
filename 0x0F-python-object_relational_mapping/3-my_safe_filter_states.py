#!/usr/bin/python3
"""This script safe from SQL injection"""
import MySQLdb
from sys import argv


def list_states():
    """my function that lists states start with N"""
    kwargs = {
        "host": "localhost",
        "port": 3306,
        "user": argv[1],
        "passwd": argv[2],
        "db": argv[3]
        }
    conn = MySQLdb.connect(**kwargs)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s ORDER BY id",
                (argv[4],))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()

if __name__ == '__main__':
    list_states()
