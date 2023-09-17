#!/usr/bin/python3
"""module that lists all cities from the database
"""
import MySQLdb
from sys import argv


def list_city(username, password, dbname, cty):
    """function that lists all cities from the database"""
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=dbname)

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s", [cty])

    rows = cur.fetchall()
    j = []
    for i in rows:
        j.append(i[1])
    print(", ".join(j))

    cur.close()
    db.close()


if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    dbname = argv[3]
    cty = argv[4]
    list_city(username, password, dbname, cty)
