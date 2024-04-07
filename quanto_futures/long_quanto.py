import matplotlib.pyplot as plt
import numpy as np

# Constants
multiplier = 0.00001  # BTC
num_contracts = 10000
prices = np.arange(0, 1050, 50)  # Prices from $0 to $1000 in steps of $50

# Calculating Bitcoin and US Dollar values
xbt_values = prices * multiplier * num_contracts
usd_values = prices**2 * multiplier * num_contracts

# Plotting with corrected X-axis labels
plt.figure(figsize=(14, 8))

# Bitcoin Values
plt.subplot(1, 2, 1)
plt.plot(prices, xbt_values, marker='o', linestyle='-', color='blue')
plt.title('Bitcoin Value of Quanto Futures Contract')
plt.xlabel('Price of Bitcoin ($)')
plt.ylabel('Bitcoin Value (XBT)')
plt.grid(True)

# US Dollar Values
plt.subplot(1, 2, 2)
plt.plot(prices, usd_values, marker='o', linestyle='-', color='red')
plt.title('US Dollar Value of Quanto Futures Contract')
plt.xlabel('Price of Bitcoin ($)')
plt.ylabel('US Dollar Value (USD)')
plt.grid(True)

plt.tight_layout()
plt.show()