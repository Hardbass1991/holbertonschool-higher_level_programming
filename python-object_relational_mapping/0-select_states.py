#!/usr/bin/python3
"""script that lists all states from a table in the database hbtn_0e_0_usa"""
if __name__ == '__main__':
    import sys
    import MySQLdb
    a = list(sys.argv)
    db = MySQLdb.connect(host="localhost", user=a[1], passwd=a[2], db=a[3])
    cur = db.cursor()
    number_of_rows = cur.execute("SELECT * FROM states ORDER BY states.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    db.close()
