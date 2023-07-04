#!/usr/bin/python3
""" search a state based on user input """
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    cur = db.cursor()
    cur.execute("""
        SELECT * FROM states
        WHERE BINARY name = '{}'
        ORDER BY id;
        """.format(sys.argv[4]))
    for row in cur.fetchall():
        print(row)
