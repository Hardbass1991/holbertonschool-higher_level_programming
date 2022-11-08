#!/usr/bin/python3
""" script that lists all cities from the database hbtn_0e_4_usa"""
if __name__ == '__main__':
    import sys
    import MySQLdb
    a = list(sys.argv)
    db = MySQLdb.connect(host="localhost", user=a[1], passwd=a[2], db=a[3])
    cur = db.cursor()
    q = """SELECT cities.id, cities.name, states.name FROM cities 
        INNER JOIN states ON cities.state_id = states.id 
        ORDER BY cities.id
    """
    number_of_rows = cur.execute(q)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    db.close()
