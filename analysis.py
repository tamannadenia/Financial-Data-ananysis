import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
connection = sqlite3.connect('../financial_data.db')

# Query to get average closing prices for each stock symbol
query = '''
SELECT symbol, AVG(close) AS average_close
FROM stocks
GROUP BY symbol
ORDER BY average_close DESC
'''
average_close = pd.read_sql(query, connection)

# Plotting average closing prices
plt.figure(figsize=(8, 5))
plt.bar(average_close['symbol'], average_close['average_close'], color='skyblue')
plt.title('Average Closing Prices of Stocks')
plt.xlabel('Stock Symbol')
plt.ylabel('Average Closing Price')
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('average_closing_prices.png')
plt.show()

# Query to get daily trading volume for a specific stock (e.g., AAPL)
symbol = 'AAPL'
query_volume = f'''
SELECT date, volume
FROM stocks
WHERE symbol = '{symbol}'
ORDER BY date
'''
trading_volume = pd.read_sql(query_volume, connection)

# Plotting trading volume over time for a specific stock
plt.figure(figsize=(8, 5))
plt.plot(trading_volume['date'], trading_volume['volume'], marker='o', linestyle='-', color='orange')
plt.title(f'Daily Trading Volume for {symbol}')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('trading_volume_aapl.png')
plt.show()

connection.close()
