#!/usr/bin/python3
""" script that lists all cities in the db in a states that matches argv[4]"""
if __name__ == '__main__':
    import sys
    import MySQLdb
    a = list(sys.argv)
    db = MySQLdb.connect(host="localhost", user=a[1], passwd=a[2], db=a[3])
    cur = db.cursor()
    q = """SELECT cities.name FROM cities
    INNER JOIN states ON cities.state_id = states.id
    WHERE states.name LIKE BINARY %s
    ORDER BY cities.id
    """
    number_of_rows = cur.execute(q, (a[4],))
    rows = cur.fetchall()
    for i in range(len(rows)):
        if i:
            print(", ", end="")
        print(rows[i][0], end="")
    print()

    db.close()
