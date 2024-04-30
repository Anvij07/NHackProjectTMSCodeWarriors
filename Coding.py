import yfinance as yf
import matplotlib.pyplot as plt

while True:
    stock=str(input("Enter the stock you want a graph for,Some examples are- AAPL,AMZN,MSFT,GOOG")).upper()
    stock_information=yf.Ticker(stock)
    prices=stock_information.history(period='1y')
    prices=prices['High']
    plt.plot(prices, marker='.', linestyle='-', color='b', label='stock price')
    plt.show()
   
