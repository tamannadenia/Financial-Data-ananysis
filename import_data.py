import sqlite3
import pandas as pd

# Read data from CSV file
data = pd.read_csv('../data/stocks_data.csv')

# Connect to SQLite database
connection = sqlite3.connect('../financial_data.db')
data.to_sql('stocks', connection, if_exists='append', index=False)

connection.close()

print("Data imported successfully into the database.")
