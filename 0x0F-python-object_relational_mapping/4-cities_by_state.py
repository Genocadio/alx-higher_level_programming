#!/usr/bin/python3
"""module that lists all states from the database"""
import MySQLdb
import sys


def getcity(username, password, database_name):
    """function that lists all cities from the database"""
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username,
                             passwd=password, db=database_name)

        cursor = db.cursor()
        cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id ASC")
        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    finally:
        cursor.close()
        db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    getcity(username, password, database_name)
