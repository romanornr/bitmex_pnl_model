import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


# User-defined parameters, you can change these values
contracts = 100  # Number of contracts
usd_contract_value = 100 # Contract value of $100
start_price = 0.1  # The starting price of Bitcoin for the plot
stop_price = 1000  # The highest price of Bitcoin to plot
num_prices = 1000  # The number of price points to plot

x_range = np.linspace(start_price, stop_price, num_prices)  # XBTUSD price range from $0.01 to $1000

# Calculations
xbt_value = (contracts * usd_contract_value) / x_range  # Inverse function: USD value / XBTUSD price

# Function to format the y-axis with 'XBT'
def xbt_formatter(x, pos):
    return f'{int(x)} XBT'

# Function to format the axis with '$'def usd_formatter(x, pos):
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

# Set the range for x and y axes
ax1.set_xlim(start_price, stop_price)
ax1.set_ylim(0, 200)  # Set the y-axis for XBT Value to go from 0 to 200   #### TODO needs fixing so that it is dynamic.. Lowest value to highest value of XBT

# Format the x-axis tick labels with a dollar sign and comma
ax1.xaxis.set_major_formatter(FuncFormatter(usd_formatter))

# Format the y-axis tick labels with 'XBT'
ax1.yaxis.set_major_formatter(FuncFormatter(xbt_formatter))

# Create the second axis (for the USD value)
ax2 = ax1.twinx()

# Plot the constant USD value
ax2.hlines(y=usd_contract_value, xmin=start_price, xmax=stop_price, colors='orange', linestyles='--', label='USD Value', linewidth=2)

# Set the y-axis label for the USD value
ax2.set_ylabel('USD Value', color='orange')

# Set the range for the second y axis
ax1.set_ylim(0, 200)  # Set the y-axis for XBT Value, the lowest value to the highest value of XBT  #### TODO needs fixing so that it is dynamic.. Lowest value to highest value of XBT

# Format the y-axis tick labels with a dollar sign and comma for the USD value
ax2.yaxis.set_major_formatter(FuncFormatter(usd_formatter))

# Show grid and legend
ax1.grid(True)
ax1.figure.legend(loc='upper center')

# Show the plot
plt.show()