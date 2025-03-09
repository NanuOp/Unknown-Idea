import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import re


# 🚀 Setup Selenium WebDriver (Headless Mode for Efficiency)
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run without opening a browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# url = "https://groww.in/stocks/castrol-india-ltd"
stock_name = input("Enter Stock Name: ").strip().lower().replace(" ", "-")
url = f"https://groww.in/stocks/{stock_name}"


driver.get(url)  # ✅ Open the URL ONCE

# 🕒 Wait for JavaScript elements to load
time.sleep(5)

# 🔹 Extract Stock Title
try:
    title = driver.find_element(By.TAG_NAME, "h1").text.strip()
    print("\nTitle:", title)
except:
    print("Title not found")

print("_________________________________________________________________________________________________________________________________________")

# 🔹 Extract Stock Price (Fixed)
try:
    price = driver.find_element(By.XPATH, "//div[contains(@class, 'lpu38Pri')]").text
    print("\nStock Price:", price)
except:
    print("Stock Price not found")

print("_________________________________________________________________________________________________________________________________________")

# 🔹 Extract Performance Data (Fixed)
html_content = driver.page_source
soup = BeautifulSoup(html_content, "html.parser")

# Extract Performance Section
try:
            performance_keys = driver.find_elements(By.XPATH, "//div[contains(@class, 'pbar29KeyText')]")
            performance_values = driver.find_elements(By.XPATH, "//div[contains(@class, 'pbar29Value')]")

            performance_data = {}

            for key, value in zip(performance_keys, performance_values):
                key_text = key.text.strip()
                value_text = value.text.strip()
                performance_data[key_text] = value_text  # Store data in dictionary

            print("\nPerformance Data:")
            for key, value in sorted(performance_data.items()):
                print(f"{key}: {value}")

except Exception as e:
            print("\nPerformance Data not found:", e)

print("_________________________________________________________________________________________________________________________________________")

# 🔹 Extract Revenue Data (Fixed)
try:
    revenue_tab = driver.find_element(By.XPATH, "//div[contains(@class, 'stkF56TabDiv') and text()='Revenue']")
    driver.execute_script("arguments[0].click();", revenue_tab)
    time.sleep(3)

    values = driver.find_elements(By.TAG_NAME, "tspan")
    numbers, months = [], []

    for value in values:
        text = value.text.strip()
        if text.replace(",", "").isdigit():
            numbers.append(text)
        else:
            months.append(text)

    revenue_data = dict(zip(months, numbers))

    print("\nRevenue Data:")
    for month, value in revenue_data.items():
        print(f"{month}: {value}")

except:
    print("\nRevenue Data not found")

print("_________________________________________________________________________________________________________________________________________")

# 🔹 Extract Profit Data (Fixed)
try:
    profit_tab = driver.find_element(By.XPATH, "//div[contains(@class, 'stkF56TabDiv') and text()='Profit']")
    driver.execute_script("arguments[0].click();", profit_tab)
    time.sleep(3)

    values = driver.find_elements(By.TAG_NAME, "tspan")

    # Separate numbers and months correctly
    numbers, months = [], []
    for value in values:
        text = value.text.strip()
        if re.match(r"^\d+[\d,]*\.?\d*$", text):  # Matches only valid numbers
            numbers.append(text)
        else:
            months.append(text)  # Consider it a month label if it's not a number

    # Ensure data is aligned properly
    profit_data = dict(zip(months, numbers))

    print("\nProfit Data:")
    for month, value in sorted(profit_data.items()):  # Sorted to maintain order
        print(f"{month}: {value}")

except Exception as e:
    print("\nProfit Data not found:", e)


print("_________________________________________________________________________________________________________________________________________")

# 🔹 Extract Net Worth Data (Not Fixed)
try:
    networth_tab = driver.find_element(By.XPATH, "//div[contains(@class, 'stkF56TabDiv') and contains(text(), 'Net Worth')]")
    driver.execute_script("arguments[0].click();", networth_tab)
    time.sleep(3)

    svg_elements = driver.find_elements(By.TAG_NAME, "svg")
    networth_svg = svg_elements[-1]  # Take the last SVG element (Net Worth)

    values = networth_svg.find_elements(By.TAG_NAME, "tspan")
    numbers, years = [], []

    for value in values:
        text = value.text.strip()
        if text.replace(",", "").isdigit():
            numbers.append(text)
        else:
            years.append(text)

    networth_data = dict(zip(years, numbers))

    if networth_data:
        print("\nNet Worth Data:")
        for year, value in networth_data.items():
            print(f"{year}: {value}")
    else:
        print("\nNet Worth Data not found")

except:
    print("\nNet Worth Data not found")

print("_________________________________________________________________________________________________________________________________________")

# 🔹 Extract "About the Stock" (Fixed)
try:
    about_section = driver.find_element(By.XPATH, "//div[contains(@class, 'aboutCompany_summary__uP8fZ')]")
    about_text = about_section.text.strip().replace("...Read more", "").strip()  # Remove "Read more" text
    print("\nAbout the Stock:\n", about_text)
except:
    print("\nAbout the Stock not found")

print("_________________________________________________________________________________________________________________________________________")

# ✅ Close Selenium properly at the end
driver.quit()
