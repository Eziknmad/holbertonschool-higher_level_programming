#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    # Create cursor and execute query
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and print all results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close cursor and connection
    cur.close()
    conn.close()
