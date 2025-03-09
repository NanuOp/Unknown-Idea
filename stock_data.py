from bsedata.bse import BSE
import io
import pandas as pd
import datetime
df = pd.read_csv("Equity.csv")  # Read the CSV file

# Create a BSE object
b = BSE()


tickers = input("Enter Stock Name:")
codes = []
codelist = ["500209", "532540"]

for code in codelist:
    try:
        quote = b.getQuote(code)  # Fetch stock data
        if quote:  # Check if data is received
            print("\nStock Information:")
            for key, value in quote.items():
                if key not in ["buy", "sell"]:  # Exclude buy & sell sections
                    print(f"{key}: {value}")
        else:
            print(f"Stock data for {code} not found.")
    except Exception as e:
        print(f"Error fetching data for {code}: {e}")

Top_gainers = b.topGainers()
print("\nToday's Top Gainers \n")
for stock in Top_gainers:
    print(f"{stock['securityID']} ({stock['scripCode']})")
    print(f"    LTP: ₹{stock['LTP']}")
    print(f"    Change: ₹{stock['change']} ({stock['pChange']}%)\n")

Top_losers = b.topLosers()
print("\nToday's Top Losers: ")
for stock in Top_losers:
    print(f"{stock['securityID']} ({stock['scripCode']})")
    print(f"    LTP: ₹{stock['LTP']}")
    print(f"    Change: ₹{stock['change']} ({stock['pChange']}%)\n")

