import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from .Gutenberg_Richter import gutenberg_richter_coefficients


def draw_montecarlo():
    # Load the data from the Excel file
    data = pd.read_excel('utils/result/relative_pga_counts.xlsx')

    # Extract the data for the x and y axes
    x_values = data['Threshold']
    y_values = data['Relative_Count']

    # Create the logarithmic curve with enhanced styling
    plt.figure(figsize=(12, 6))  # Create a single figure with multiple subplots

    # Montecarlo Plot
    plt.subplot(1, 2, 1)  # Create the first subplot
    plt.loglog(x_values, y_values, marker='o', color='b', linestyle='-', linewidth=2, markersize=8, label='Annual Exceedance Probability')
    plt.title('PSHA', fontsize=16)
    plt.xlabel('Log(PGA)', fontsize=12)
    plt.ylabel('Annual Exceedance Probability', fontsize=12)
    plt.xticks(x_values, labels=["{:.2f}".format(val) for val in x_values])
    plt.legend()
    plt.grid(True, which="both", linestyle='--', lw=0.5, color='gray')
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)

    a, b, magnitudes, log_counts, min_magnitude, max_magnitude = gutenberg_richter_coefficients()

    # Gutenberg-Richter Plot
    plt.subplot(1, 2, 2)  # Create the second subplot
    plt.plot(magnitudes, log_counts, 'o', label='Data')
    plt.plot(magnitudes, a - b * np.array(magnitudes), label=f'Gutenberg-Richter Fit: a={a:.2f}, b={b:.2f}')
    plt.xlabel('Magnitude')
    plt.ylabel('log(N)')
    plt.legend()
    plt.title('Gutenberg-Richter Distribution')
    plt.grid()

    # Adjust layout to prevent overlap
    plt.tight_layout()

    # Display the plot
    plt.show()
