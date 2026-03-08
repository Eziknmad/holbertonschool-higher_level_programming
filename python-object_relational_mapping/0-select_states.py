#!/usr/bin/env python3
"""
Module that lists all states from the database hbtn_0e_0_usa.
This script connects to MySQL and retrieves all states sorted by id.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to MySQL server
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )

    # Create cursor to execute queries
    cur = conn.cursor()

    # Execute query to get all states sorted by id
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all results
    query_rows = cur.fetchall()

    # Print each row
    for row in query_rows:
        print(row)

    # Close cursor and connection
    cur.close()
    conn.close()
