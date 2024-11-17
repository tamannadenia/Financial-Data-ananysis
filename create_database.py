import sqlite3

# Connect to SQLite database
connection = sqlite3.connect('../financial_data.db')
cursor = connection.cursor()

# Create table for storing stock data
cursor.execute('''
CREATE TABLE IF NOT EXISTS stocks (
    date TEXT,
    symbol TEXT,
    open REAL,
    high REAL,
    low REAL,
    close REAL,
    volume INTEGER
)
''')

connection.commit()
connection.close()

print("Database and table created successfully.")
