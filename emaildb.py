"""
Project: Email Domain Counter using SQLite
Author: Anup Sharma
Description:
This project reads an mbox email file, extracts the domain names
from email addresses, and stores the count of each domain in an SQLite database.
It demonstrates file handling, string manipulation, and database operations in Python.
"""

import sqlite3

# -------------------- Step 1: Connect to SQLite --------------------
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# -------------------- Step 2: Create Table --------------------
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

# -------------------- Step 3: Read file --------------------
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox.txt'

# -------------------- Step 4: Process file line by line --------------------
with open(fname) as fh:
    for line in fh:
        if not line.startswith('From: '):
            continue
        pieces = line.split()
        email = pieces[1]
        domain = email.split('@')[1]

        # Check if domain exists in DB
        cur.execute('SELECT count FROM Counts WHERE org = ?', (domain,))
        row = cur.fetchone()

        # Insert or update domain count
        if row is None:
            cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (domain,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (domain,))

# -------------------- Step 5: Commit changes --------------------
conn.commit()
print("✅ Data committed to emaildb.sqlite successfully!")
