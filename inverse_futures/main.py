import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Constants
usd_contract_value = 10000
x_range = np.linspace(0.01, 1000, 10000)  # XBTUSD price range from $0.01 to $1000

# Calculations
xbt_value = usd_contract_value / x_range  # Inverse function: USD value / XBTUSD price

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
ax1.set_xlim(0, 1000)
ax1.set_ylim(0, 200)  # Set the y-axis for XBT Value to go from 0 to 200

# Format the x-axis tick labels with a dollar sign and comma
ax1.xaxis.set_major_formatter(FuncFormatter(usd_formatter))

# Format the y-axis tick labels with 'XBT'
ax1.yaxis.set_major_formatter(FuncFormatter(xbt_formatter))

# Create the second axis (for the USD value)
ax2 = ax1.twinx()

# Plot the constant USD value
ax2.hlines(y=usd_contract_value, xmin=0, xmax=1000, colors='orange', linestyles='--', label='USD Value', linewidth=2)

# Set the y-axis label for the USD value
ax2.set_ylabel('USD Value', color='orange')

# Set the range for the second y axis
ax2.set_ylim(0, 20000)

# Format the y-axis tick labels with a dollar sign and comma for the USD value
ax2.yaxis.set_major_formatter(FuncFormatter(usd_formatter))

# Show grid and legend
ax1.grid(True)
ax1.figure.legend(loc='upper center')

# Show the plot
plt.show()