import nselib
from nselib import capital_market


a = nselib.trading_holiday_calendar()
# date = input("Enter a date: ")
# month = input("Enter Month: (as number)")
# year = input("Enter a year: ")


b = capital_market.bhav_copy_equities('1-03-2025')
print(b)
# c = capital_market.bhav_copy_with_delivery('1-03-2025')
# # print(c)
# period_of_months = input("Number of Months(Do add M at last): ")
# # d = capital_market.block_deals_data(period='1M')
# # print(d)
# Companys = input("Stock: ")
# e = capital_market.deliverable_position_data(f'{Companys}',period=f'{period_of_months}')
print("\nEquity List\n")
f = capital_market.equity_list()
print(f)
print("\n F&O Equity List\n")
g = capital_market.fno_equity_list()
print(g)
# h = capital_market.index_data()
# print(h)
print("\n Nifty 50 Companys\n")
i = capital_market.nifty50_equity_list()
print(i)
j = capital_market.week_52_high_low_report()
