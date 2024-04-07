import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Entry prices and multipliers from the spreadsheet
entry_price_quanto = 500
multiplier_quanto = 0.00001
contracts_quanto = 4000

entry_price_inverse = 500
multiplier_inverse = 100
contracts_inverse = 100

# XBTUSD values from $0 to $1000, increment by $50
xbtusd_values = np.arange(0, 1050, 50)

# Adjusted PNL calculations based on the provided formulas
quanto_xbt_pnl = (xbtusd_values - entry_price_quanto) * multiplier_quanto * contracts_quanto
quanto_usd_pnl = quanto_xbt_pnl * xbtusd_values
inverse_xbt_pnl = (1 / entry_price_inverse - 1 / xbtusd_values) * multiplier_inverse * contracts_inverse
inverse_usd_pnl = inverse_xbt_pnl * xbtusd_values

# Creating a DataFrame with the PNL data
pnl_data = pd.DataFrame({
    'XBTUSD': xbtusd_values,
    'Quanto XBT PNL': quanto_xbt_pnl,
    'Quanto USD PNL': quanto_usd_pnl,
    'Inverse XBT PNL': inverse_xbt_pnl,
    'Inverse USD PNL': inverse_usd_pnl
})

def plot_pnl_graphs_with_dual_axis_grid_legend(df):
    fig, axs = plt.subplots(1, 2, figsize=(18, 6))

    # Quanto Return Profile with Grid and Legend
    ax1 = axs[0]
    color = 'tab:red'
    ln1 = ax1.plot(df['XBTUSD'], df['Quanto USD PNL'], label='Quanto USD PNL', color=color)
    ax1.set_xlabel('XBTUSD Price ($)')
    ax1.set_ylabel('Quanto USD PNL', color=color)
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.grid(True)
    ax1.set_title('Quanto Return Profile')
    ax1.yaxis.set_major_formatter(plt.FuncFormatter('${:,.0f}'.format))

    ax2 = ax1.twinx()
    color = 'tab:blue'
    ln2 = ax2.plot(df['XBTUSD'], df['Quanto XBT PNL'], label='Quanto XBT PNL', color=color)
    ax2.set_ylabel('Quanto XBT PNL', color=color)
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.yaxis.set_major_formatter(plt.FuncFormatter('{:,.0f} XBT'.format))

    # Adding legend manually to handle dual axes
    lns = ln1 + ln2
    labels = [l.get_label() for l in lns]
    ax1.legend(lns, labels, loc='upper left')

    # Inverse Return Profile with Grid and Legend
    ax3 = axs[1]
    color = 'tab:red'
    ln3 = ax3.plot(df['XBTUSD'], df['Inverse USD PNL'], label='Inverse USD PNL', color=color)
    ax3.set_xlabel('XBTUSD Price ($)')
    ax3.set_ylabel('Inverse USD PNL', color=color)
    ax3.tick_params(axis='y', labelcolor=color)
    ax3.grid(True)
    ax3.set_title('Inverse Return Profile')
    ax3.yaxis.set_major_formatter(plt.FuncFormatter('${:,.0f}'.format))

    ax4 = ax3.twinx()
    color = 'tab:blue'
    ln4 = ax4.plot(df['XBTUSD'], df['Inverse XBT PNL'], label='Inverse XBT PNL', color=color)
    ax4.set_ylabel('Inverse XBT PNL', color=color)
    ax4.tick_params(axis='y', labelcolor=color)
    ax4.yaxis.set_major_formatter(plt.FuncFormatter('{:,.0f} XBT'.format))

    # Adding legend manually to handle dual axes
    lns = ln3 + ln4
    labels = [l.get_label() for l in lns]
    ax3.legend(lns, labels, loc='upper left')

    fig.tight_layout()
    plt.show()

# Assuming the pnl_data DataFrame exists and is correctly set up
plot_pnl_graphs_with_dual_axis_grid_legend(pnl_data)