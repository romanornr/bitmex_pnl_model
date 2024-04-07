import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.ticker import FuncFormatter

# Entry prices and multipliers from the spreadsheet
entry_price_quanto = 500
multiplier_quanto = 0.00001
contracts_quanto = 4000

entry_price_inverse = 500
multiplier_inverse = 100
contracts_inverse = 100

# XBTUSD values from $0 to $1050, increment by $50
xbtusd_values = np.arange(0, 1050, 50)

# Adjusted PNL calculations based on the provided formulas
quanto_xbt_pnl = (xbtusd_values - entry_price_quanto) * multiplier_quanto * contracts_quanto
quanto_usd_pnl = quanto_xbt_pnl * xbtusd_values
inverse_xbt_pnl = (1 / entry_price_inverse - 1 / xbtusd_values) * multiplier_inverse * contracts_inverse
inverse_usd_pnl = inverse_xbt_pnl * xbtusd_values

# Calculating PNL for "Long quanto vs. Short inverse" and "Long inverse vs. Short Quanto"
long_quanto_short_inverse_xbt_pnl = quanto_xbt_pnl - inverse_xbt_pnl
long_quanto_short_inverse_usd_pnl = quanto_usd_pnl - inverse_usd_pnl

long_inverse_short_quanto_xbt_pnl = inverse_xbt_pnl - quanto_xbt_pnl
long_inverse_short_quanto_usd_pnl = inverse_usd_pnl - quanto_usd_pnl

# Creating a DataFrame for the new PNL calculations
pnl_comparison_data = pd.DataFrame({
    'XBTUSD': xbtusd_values,
    'Long Quanto vs. Short Inverse XBT PNL': long_quanto_short_inverse_xbt_pnl,
    'Long Quanto vs. Short Inverse USD PNL': long_quanto_short_inverse_usd_pnl,
    'Long Inverse vs. Short Quanto XBT PNL': long_inverse_short_quanto_xbt_pnl,
    'Long Inverse vs. Short Quanto USD PNL': long_inverse_short_quanto_usd_pnl
})

# Function to format the tick labels
def usd_formatter(x, pos):
    return '${:,.0f}'.format(x)  # Format as dollar value, no decimal places

def xbt_formatter(x, pos):
    return '{:,.0f} XBT'.format(x)  # Format as integer followed by "XBT"

# Adjusted plotting function for the new comparison graphs with formatted y-axes
def plot_comparison_graphs(df):
    fig, axs = plt.subplots(1, 2, figsize=(18, 6))

    # Long Quanto vs. Short Inverse
    ax1 = axs[0]
    ax1.plot(df['XBTUSD'], df['Long Quanto vs. Short Inverse USD PNL'], label='USD PNL', color='green')
    ax1.set_xlabel('XBTUSD Price')
    ax1.set_ylabel('Long Quanto vs. Short Inverse USD PNL', color='green')
    ax1.tick_params(axis='y', labelcolor='green')
    ax1.grid(True)
    ax1.set_title('Long Quanto vs. Short Inverse')
    ax1.legend(loc='upper left')
    ax1.yaxis.set_major_formatter(FuncFormatter(usd_formatter))

    ax2 = ax1.twinx()
    ax2.plot(df['XBTUSD'], df['Long Quanto vs. Short Inverse XBT PNL'], label='XBT PNL', color='blue')
    ax2.set_ylabel('Long Quanto vs. Short Inverse XBT PNL', color='blue')
    ax2.tick_params(axis='y', labelcolor='blue')
    ax2.legend(loc='upper right')
    ax2.yaxis.set_major_formatter(FuncFormatter(xbt_formatter))

    # Long Inverse vs. Short Quanto
    ax3 = axs[1]
    ax3.plot(df['XBTUSD'], df['Long Inverse vs. Short Quanto USD PNL'], label='USD PNL', color='green')
    ax3.set_xlabel('XBTUSD Price')
    ax3.set_ylabel('Long Inverse vs. Short Quanto USD PNL', color='green')
    ax3.tick_params(axis='y', labelcolor='green')
    ax3.grid(True)
    ax3.set_title('Long Inverse vs. Short Quanto')
    ax3.legend(loc='upper left')
    ax3.yaxis.set_major_formatter(FuncFormatter(usd_formatter))

    ax4 = ax3.twinx()
    ax4.plot(df['XBTUSD'], df['Long Inverse vs. Short Quanto XBT PNL'], label='XBT PNL', color='blue')
    ax4.set_ylabel('Long Inverse vs. Short Quanto XBT PNL', color='blue')
    ax4.tick_params(axis='y', labelcolor='blue')
    ax4.legend(loc='upper right')
    ax4.yaxis.set_major_formatter(FuncFormatter(xbt_formatter))

    fig.tight_layout()
    plt.show()

# Call the function to plot the comparison graphs
plot_comparison_graphs(pnl_comparison_data)

