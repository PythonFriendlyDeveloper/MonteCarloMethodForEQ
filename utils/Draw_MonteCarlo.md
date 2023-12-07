# Montecarlo Plot with Gutenberg-Richter Distribution

This Python script generates a Montecarlo plot and a Gutenberg-Richter distribution plot using earthquake data.

## Dependencies

- [pandas](https://pandas.pydata.org/): For data manipulation.
- [numpy](https://numpy.org/): For mathematical operations.
- [matplotlib](https://matplotlib.org/): For creating plots.
- `Gutenberg_Richter.gutenberg_richter_coefficients`: A custom function for Gutenberg-Richter calculations (assuming it's in the same package).

Make sure you have these libraries installed before running the script.

## Code

```python
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
    plt.semilogx(x_values, y_values, marker='o', color='b', linestyle='-', linewidth=2, markersize=8, label='Annual Exceedance Probability')
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
```

## Usage

1. Ensure you have the required Python libraries installed.
2. Make sure you have the `utils/result/relative_pga_counts.xlsx` file with the necessary data.
3. Call the `draw_montecarlo()` function to generate Montecarlo and Gutenberg-Richter plots.

## Description

- The script loads data from an Excel file, `relative_pga_counts.xlsx`, for the Montecarlo plot.
- It also uses the `gutenberg_richter_coefficients()` function to obtain Gutenberg-Richter distribution coefficients ('a' and 'b').
- Two subplots are created in a single figure, one for the Montecarlo plot and the other for the Gutenberg-Richter plot.
- The Montecarlo plot displays annual exceedance probability on a logarithmic scale.
- The Gutenberg-Richter plot shows the distribution of earthquake magnitudes and a linear fit.
- The resulting plots are displayed using Matplotlib.

Feel free to modify and adapt this script to your specific data and analysis needs.
