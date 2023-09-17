#!/usr/bin/python3
"""module that lists all states from the database
"""
import MySQLdb
import sys


def get_Nstates(username, password, database_name):
    """function that lists all states from the database"""
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database_name)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name\
                LIKE BINARY 'N%' ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    get_Nstates(username, password, database_name)
