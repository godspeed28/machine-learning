# SQL Data Imports 
from pymongo import MongoClient
import pandas as pd

# Create a MongoDB client
con = MongoClient()

# Chose database (con.list_database_names() to see all databases)
db = con.database_names

# Define the query (empty dict selects all documents)
query = {}

# Create a cursor object using query
cursor = db.collection_name.find(query)

# Expand the cursor and construct the DataFrame
data = pd.DataFrame(list(cursor))

