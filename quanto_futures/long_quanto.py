import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

# user defined parameters. For the multiplier of a specific contract, you can find it in the contract specifications of Bitmex documentation
multiplier = 0.00001	# BTC multiplier
num_contracts = 10000	# Number of contracts
start_price = 0		# Starting price of Bitcoin
end_price = 1050	# Ending price of Bitcoin
step_price = 50		# Step size between prices

# Automatically generated array of Bitcoin prices based on user-defined settings
prices = np.arange(start_price, end_price + step_price, step_price)

def dollar_formatter(x, pos):
    """
    Custom formatter to convert numbers to dollar format.
    
    :param x: The tick value.
    :param pos: The position (unused, but required by FuncFormatter).
    :return: The formatted tick label as a string.
    """
    return f'${x:,.0f}'

def xbt_formatter(x, pos):
    """
    Custom formatter to append 'XBT' to the tick values.
    
    :param x: The tick value.
    :param pos: The position (unused, but required by FuncFormatter).
    :return: The formatted tick label as a string with 'XBT'.
    """
    return f'{x:,.0f} XBT'

def calculate_values(prices, multiplier, num_contracts):
    """
    Calculate the Bitcoin and US Dollar values of Quanto futures contracts.
    
    :param prices: Array of Bitcoin prices
    :param multiplier: Contract size multiplier
    :param num_contracts: Number of contracts
    :return: Tuple of arrays (Bitcoin values, USD values)
    """
    xbt_values = prices * multiplier * num_contracts
    usd_values = prices**2 * multiplier * num_contracts
    return xbt_values, usd_values

def plot_values(prices, xbt_values, usd_values):
    """
    Plot the Bitcoin and US Dollar values of Quanto futures contracts.
    
    :param prices: Array of Bitcoin prices
    :param xbt_values: Bitcoin values of contracts
    :param usd_values: USD values of contracts
    """
    plt.figure(figsize=(14, 8))
    dollar_format = FuncFormatter(dollar_formatter)
    xbt_format = FuncFormatter(xbt_formatter)

    # Bitcoin Values
    plt.subplot(1, 2, 1)
    plt.plot(prices, xbt_values, marker='o', linestyle='-', color='blue')
    plt.title('Bitcoin Value of Quanto Futures Contract')
    plt.xlabel('Price of Bitcoin ($)')
    plt.ylabel('Bitcoin Value')
    plt.grid(True)
    plt.gca().xaxis.set_major_formatter(dollar_format)
    plt.gca().yaxis.set_major_formatter(xbt_format)

    # US Dollar Values
    plt.subplot(1, 2, 2)
    plt.plot(prices, usd_values, marker='o', linestyle='-', color='red')
    plt.title('US Dollar Value of Quanto Futures Contract')
    plt.xlabel('Price of Bitcoin ($)')
    plt.ylabel('US Dollar Value (USD)')
    plt.grid(True)
    plt.gca().xaxis.set_major_formatter(dollar_format)
    plt.gca().yaxis.set_major_formatter(dollar_format)

    plt.tight_layout()
    plt.show()


# Calculate and plot values
xbt_values, usd_values = calculate_values(prices, multiplier, num_contracts)
plot_values(prices, xbt_values, usd_values)