import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


# User-defined parameters, you can change these values
contracts = 100  # Number of contracts
usd_contract_value = 100 # Contract value of $100
start_price = 0.1  # The starting price of Bitcoin for the plot
stop_price = 1000  # The highest price of Bitcoin to plot
num_prices = 1000  # The number of price points to plot

# Constants
usd_contract_value = contracts * usd_contract_value  # Total USD value of the contracts

x_range = np.linspace(0.01, 1000, 10000)  # Ensuring x_range does not include zero to avoid division by zero.

# Calculations
xbt_value = usd_contract_value / x_range  # Inverse function: USD value / XBTUSD price

# Function to format the y-axis with 'XBT'
def xbt_formatter(x, pos):
    return f'{int(x)} XBT'

# Function to format the axis with '$'
def usd_formatter(x, pos):
    return f'${int(x):,}'

# Create the figure and the first axis (for the XBT value)
fig, ax1 = plt.subplots(figsize=(10, 5))

# Plot the XBT value against XBTUSD with a thicker line for visibility
ax1.plot(x_range, xbt_value, color='blue', label='XBT Value', linewidth=2)

# Set the x-axis label and y-axis label for the XBT value
ax1.set_xlabel('XBTUSD Price')
ax1.set_ylabel('XBT Value', color='blue')
ax1.set_title('Inverse Return Profile for XBT Futures')

# Formatting the tick labels
ax1.xaxis.set_major_formatter(FuncFormatter(usd_formatter))
ax1.yaxis.set_major_formatter(FuncFormatter(xbt_formatter))

# Set the range for x and y axes
ax1.set_ylim(0, 200)

# Create the second axis (for the USD value)
ax2 = ax1.twinx()
ax2.hlines(y=usd_contract_value, xmin=start_price, xmax=stop_price, colors='orange', linestyles='--', label='USD Value', linewidth=2)
ax2.set_ylabel('USD Value', color='orange')
ax2.set_ylim(0, 20000)
ax2.yaxis.set_major_formatter(FuncFormatter(usd_formatter))

ax1.grid(True)

# Combined legend for both ax1 and ax2
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='upper center')


plt.show()
