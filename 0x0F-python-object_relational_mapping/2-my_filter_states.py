#!/usr/bin/python3
"""module that lists all states from the database"""
import MySQLdb
import sys


def search_states(username, password, dbname, state_name):
    """function that lists all states from the database"""
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=dbname)

    cursor = db.cursor()

    sql_query = "SELECT * FROM states WHERE name = %s ORDER BY states.id"
    cursor.execute(sql_query, (state_name,))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    search_states(username, password, dbname, state_name)
