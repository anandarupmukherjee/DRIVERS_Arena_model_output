#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 11:29:42 2023

@author: anandarupmukherjee
"""

import sqlite3
import socket

# Define the server address and port
SERVER_ADDRESS = '20.121.204.44'
SERVER_PORT = 12345

# Connect to the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.connect((SERVER_ADDRESS, SERVER_PORT))

# Connect to the database
conn = sqlite3.connect('2023-02-20_Overall_Process_AP.db')

# Get a cursor object
cur = conn.cursor()

# Execute a query to get a list of all tables in the database
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Fetch all the results
tables = cur.fetchall()

# Loop through each table and read its contents
for table in tables:
    table_name = table[0]
    print("Table:", table_name)
    cur.execute(f"SELECT * FROM {table_name}")
    rows = cur.fetchall()
    for row in rows:
        # Send each row to the server as a string
        row_str = str(row)
        server_socket.sendall(row_str.encode())

# Close the cursor and the database connection
cur.close()
conn.close()

# Close the server connection
server_socket.close()
