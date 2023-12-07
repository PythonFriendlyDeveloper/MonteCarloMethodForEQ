import pandas as pd
import numpy as np
from scipy.stats import linregress

def gutenberg_richter_coefficients():
    # Load data from the Excel file
    file_path = 'utils/data/main_earthquake.xlsx'
    df = pd.read_excel(file_path, engine='openpyxl')

    # Extract magnitude values from the "Magnitude" column
    magnitudes = df['Mw'].tolist()

    # Count the number of earthquakes for each magnitude
    unique_magnitudes = sorted(set(magnitudes))
    counts = [(df['Mw'] >= m).sum() for m in unique_magnitudes]

    # Calculate the logarithm of the counts
    log_counts = [np.log10(count) for count in counts]

    # Fit a linear regression model
    slope, intercept, r_value, p_value, std_err = linregress(unique_magnitudes, log_counts)

    # Extract 'a' and 'b' coefficients
    a = intercept
    b = -slope

    # Find the minimum and maximum magnitude values
    min_magnitude = min(magnitudes)
    max_magnitude = max(magnitudes)

    return a, b, unique_magnitudes, log_counts, min_magnitude, max_magnitude
