#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 11:38:03 2023

@author: anandarupmukherjee
"""

import sqlite3
import json
import socket

# Define the remote socket server's address and port
REMOTE_SERVER_ADDRESS = '20.121.204.44'
REMOTE_SERVER_PORT = 12345

# Connect to the database
conn = sqlite3.connect('2023-02-20_Overall_Process_AP.db')

# Get a cursor object
cur = conn.cursor()

# Execute a query to get a list of all tables in the database
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Fetch all the results
tables = cur.fetchall()

# Create an empty dictionary to store the JSON data
data = {}

# Loop through each table and read its contents
for table in tables:
    table_name = table[0]
    print("Table:", table_name)
    cur.execute(f"SELECT * FROM {table_name}")
    rows = cur.fetchall()
    data[table_name] = [list(row) for row in rows]

# Close the cursor and the database connection
cur.close()
conn.close()

# Convert the data to JSON
json_data = json.dumps(data)

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the remote socket server
s.connect((REMOTE_SERVER_ADDRESS, REMOTE_SERVER_PORT))

# Send the JSON data to the remote socket server
s.send(json_data.encode())

# Close the socket
s.close()
