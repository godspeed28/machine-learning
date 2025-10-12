# SQL Data Imports
import pandas as pd
import sqlite3 as sq3

# Initialize path to database
db_path = 'data/classic_rock.db'

# Create a connection to the database
conn = sq3.Connection(db_path)

# Write the query
query = "SELECT * FROM rock_songs"

# Excecute query
data = pd.read_sql_query(query, conn)

# print(data.head()) # artinya print 5 rows pertama

print(data) # print all rows
