import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Define the ticker symbol and timeframe
ticker_symbol = "AC"

# Fetch historical market data
data = yf.download(ticker_symbol, start="2024-01-01", end="2025-01-01")

# Compute short and long-term moving averages
short_window = 5
long_window = 10

data['Short_MA'] = data['Close'].rolling(window=short_window, min_periods=1).mean()
data['Long_MA'] = data['Close'].rolling(window=long_window, min_periods=1).mean()

# Generate buy/sell signals
data['Signal'] = 0
data['Signal'][short_window:] = np.where(data['Short_MA'][short_window:] > data['Long_MA'][short_window:], 1, 0)
data['Position'] = data['Signal'].diff()

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(data['Close'], label='Price')
plt.plot(data['Short_MA'], label='Short MA')
plt.plot(data['Long_MA'], label='Long MA')

plt.title('Moving Average Crossover Strategy for ' + ticker_symbol)
plt.legend()
plt.show()
