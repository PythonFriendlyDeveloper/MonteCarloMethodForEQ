# Gutenberg-Richter Coefficients Calculation

This Python script calculates the Gutenberg-Richter coefficients 'a' and 'b' using earthquake magnitude data from an Excel file. It also provides other related information about the data.

## Dependencies

- [pandas](https://pandas.pydata.org/): For data manipulation.
- [numpy](https://numpy.org/): For mathematical operations.
- [scipy.stats.linregress](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html): For performing linear regression.

Make sure you have these libraries installed before running the script.

## Code

```python
import pandas as pd
import numpy as np
from scipy.stats import linregress

def gutenberg_richter_coefficients():
    # Load data from the Excel file
    file_path = 'utils/data/Gutenberg-Richter.xlsx'
    df = pd.read_excel(file_path, engine='openpyxl')

    # Extract magnitude values from the "Magnitude" column
    magnitudes = df['Magnitude'].tolist()

    # Count the number of earthquakes for each magnitude
    unique_magnitudes = sorted set(magnitudes))
    counts = [(df['Magnitude'] >= m).sum() for m in unique_magnitudes]

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
```
## Usage

1. Ensure you have the required Python libraries installed.
2. Place your earthquake magnitude data in an Excel file at the path 'utils/data/Gutenberg-Richter.xlsx'.
3. Call the `gutenberg_richter_coefficients()` function to obtain the 'a' and 'b' coefficients and other related information.

## Results

- `a`: Intercept of the linear regression line.
- `b`: Slope of the linear regression line.
- `unique_magnitudes`: Unique magnitude values in the dataset.
- `log_counts`: Logarithm of earthquake counts for each unique magnitude.
- `min_magnitude`: Minimum magnitude value in the dataset.
- `max_magnitude`: Maximum magnitude value in the dataset.

You can use these coefficients to describe the Gutenberg-Richter distribution for your earthquake data.

