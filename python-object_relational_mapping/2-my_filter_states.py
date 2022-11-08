#!/usr/bin/python3
"""script that lists all states named as argv[4]"""
if __name__ == '__main__':
    import sys
    import MySQLdb
    a = list(sys.argv)
    db = MySQLdb.connect(host="localhost", user=a[1], passwd=a[2], db=a[3])
    cur = db.cursor()
    q = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id"
    q = q.format(a[4])
    number_of_rows = cur.execute(q)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    db.close()
