import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.ticker import FuncFormatter


quanto_premium = 100
xbt_usd_price = 500

# Entry prices and multipliers from the spreadsheet
entry_price_quanto = xbt_usd_price + quanto_premium
multiplier_quanto = 0.00001

entry_price_inverse = xbt_usd_price
multiplier_inverse = 100
contracts_inverse = 100

# calculations for the inverse contract values
inverse_usd_value = multiplier_inverse * contracts_inverse
inverse_xbt_value = inverse_usd_value / entry_price_inverse

# calculations for the quanto contract values
contracts_quanto = inverse_xbt_value  / (entry_price_quanto * multiplier_quanto)
quanto_usd_value = contracts_quanto * multiplier_quanto * (entry_price_quanto ** 2)

# XBTUSD values from $50 to $1050, increment by $50. Start from $50 to avoid division by zero
xbtusd_values = np.arange(50, 1050, 50)

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

    # Determine the common y-axis limits for better comparison
    all_pnl_values = pd.concat([df['Long Quanto vs. Short Inverse USD PNL'], df['Long Quanto vs. Short Inverse XBT PNL'],
                                df['Long Inverse vs. Short Quanto USD PNL'], df['Long Inverse vs. Short Quanto XBT PNL']])
    min_pnl, max_pnl = all_pnl_values.min(), all_pnl_values.max()
    common_ylim = (min_pnl - (0.1 * abs(min_pnl)), max_pnl + (0.1 * abs(max_pnl)))  # Adjusting limits for margin

    # Plotting with adjusted y-axis limits
    for i, scenario in enumerate(['Long Quanto vs. Short Inverse', 'Long Inverse vs. Short Quanto']):
        ax1 = axs[i]
        ax1.plot(df['XBTUSD'], df[f'{scenario} USD PNL'], label='USD PNL', color='green')
        ax1.set_xlabel('XBTUSD Price')
        ax1.set_ylabel(f'{scenario} USD PNL', color='green')
        ax1.tick_params(axis='y', labelcolor='green')
        ax1.grid(True)
        ax1.set_title(scenario)
        ax1.legend(loc='upper left')
        ax1.yaxis.set_major_formatter(FuncFormatter(usd_formatter))
        ax1.set_ylim(common_ylim)  # Set common y-axis limits for USD PNL

        ax2 = ax1.twinx()
        ax2.plot(df['XBTUSD'], df[f'{scenario} XBT PNL'], label='XBT PNL', color='blue')
        ax2.set_ylabel(f'{scenario} XBT PNL', color='blue')
        ax2.tick_params(axis='y', labelcolor='blue')
        ax2.legend(loc='upper right')
        ax2.yaxis.set_major_formatter(FuncFormatter(xbt_formatter))
        ax2.set_ylim(common_ylim)  # Set common y-axis limits for XBT PNL

    fig.tight_layout()
    plt.show()


# Call the function to plot the comparison graphs
plot_comparison_graphs(pnl_comparison_data)

