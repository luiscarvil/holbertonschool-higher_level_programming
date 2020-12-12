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
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id WHERE states.name=%s "
        "ORDER BY cities.id ", (argv[4], )
        )
    row = cur.fetchall()
    cities_str = []
    cont = 0
    for i in row:
        cities_str.append(row[cont][0])
        cont += 1
    only_words = ", ".join(cities_str)
    print(only_words)
    cur.close()
    db.close()
