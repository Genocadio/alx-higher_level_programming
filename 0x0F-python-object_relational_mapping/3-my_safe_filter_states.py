#!/usr/bin/python3
"""module that lists all states from the database"""
import MySQLdb
from sys import argv


def filter_states(username, password, dbname, stte):
    """function that lists all states from the database"""
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=dbname)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = %s", [stte])

    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    db.close()


if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    dbname = argv[3]
    stte = argv[4]
    filter_states(username, password, dbname, stte)
