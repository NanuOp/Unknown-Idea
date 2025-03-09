from bsedata.bse import BSE
import io
import pandas as pd
df = pd.read_csv('Equity.csv',)  # Read the CSV file

# Create a BSE object
b = BSE()

tickers = ['INFY', 'TCS', 'Castrol']
codes = []

for ticker in tickers:
    try:
        code = df[df['Security Id'] == ticker]['Security Code'].values[0]  # Get the security code
        codes.append(str(code))  # Convert to string and add to the list
    except IndexError:
        print(f"Ticker {ticker} not found in CSV file.")

print("Extracted Codes:", codes)  # Print the extracted codes