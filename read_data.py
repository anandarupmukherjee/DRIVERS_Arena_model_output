#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 11:06:37 2023

@author: anandarupmukherjee
"""

import sqlite3

import pandas as pd
import sqlalchemy 

try:
    conn = sqlite3.connect('2023-02-20_Overall_Process_AP.db')    
except Exception as e:
    print(e)

#Now in order to read in pandas dataframe we need to know table name
cur = conn.cursor()
# Execute a query to get a list of all tables in the database
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Fetch all the results
tables = cur.fetchall()

# Print the report header
print("Report of all tables in the database:\n")

# Print the table names
for table in tables:
    table_name = table[0]
    print("Table:", table_name)
    cur.execute(f"SELECT * FROM {table_name}")
    rows = cur.fetchall()
    for row in rows:
        print(row)

# Print the report footer
print("\nTotal tables: ", len(tables))



cur.execute("PRAGMA table_info(Statistic);")
print(cur.fetchall())


cur.execute("PRAGMA table_info(Scenario);")
print(cur.fetchall())

cur.execute("PRAGMA table_info(Definition);")
print(cur.fetchall())


cur.execute("PRAGMA table_info(Output);")
print(cur.fetchall())
# Close the cursor and the database connection
cur.close()
conn.close()

