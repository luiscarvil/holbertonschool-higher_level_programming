#!/usr/bin/python3
""" import and print database MySQL """
import MySQLdb
from sys import argv
if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        db=argv[3]
    )
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states where name='{:s}' ORDER BY states.id".format(
            argv[4]
        )
    )
    rows = cur.fetchall()
    for i in rows:
        if i[1] == argv[4]:
            print(i)
    cur.close()
    db.close()
