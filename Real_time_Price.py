import time
import requests
from bs4 import BeautifulSoup

# Get user input
ticker = input("Enter the stock symbol: ").strip().upper()
exchange = input("Enter exchange (NSE or BSE): ").strip().upper()

# Validate exchange input
if exchange not in ["NSE", "BSE"]:
    print("Invalid exchange. Defaulting to BSE.")
    exchange = "NSE"


url1 = f"https://www.google.com/finance/quote/{ticker}:{exchange}?hl=en"

responce = requests.get(url1) 
for i in range(1000):
    soup = BeautifulSoup(responce.text, 'html.parser')
    class1 = "YMlKec fxKbKc"
    price = soup.find('div', class_=class1)
    price = price.text.strip()[1:].replace(",", "")
    print(f"{price}")

time.sleep(10)


