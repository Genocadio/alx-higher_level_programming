#!/usr/bin/python3
"""module that lists all states from the database
"""
import MySQLdb
import sys


def get_states(username, password, database_name):
    """function that lists all states from the database
    @param username: username of sql user
    @param password: password of sql user
    @param database_name: name of database
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database_name)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./list_states.py <username> <password> <database_name>")
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    get_states(username, password, database_name)
