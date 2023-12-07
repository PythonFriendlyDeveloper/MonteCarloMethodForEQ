# Montecarlo Count Calculation

This Python script calculates relative counts based on specified threshold values using data from an Excel file. It then saves the calculated data to another Excel file.

## Dependencies

- [pandas](https://pandas.pydata.org/): For data manipulation.

Make sure you have the required `pandas` library installed before running the script.

## Code

```python
import pandas as pd

def count_montecarlo():
    # Load the data from the Excel file
    data = pd.read_excel('utils/result/random_data.xlsx')

    # List of threshold values
    thresholds = [0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

    # Initialize an empty list to store the relative counts
    relative_counts = []

    # Calculate the relative counts for each threshold
    total_rows = len(data)  # Get the total number of rows
    for threshold in thresholds:
        count = (data['PGA'] >= threshold).sum()  # Count PGA values greater than or equal to the threshold
        relative_count = count / total_rows  # Calculate the relative count
        relative_counts.append(relative_count)

    # Create a DataFrame for the relative counts
    count_data = pd.DataFrame({'Threshold': thresholds, 'Relative_Count': relative_counts})

    # Save the count_data DataFrame to a new Excel file
    count_data.to_excel('utils/result/relative_pga_counts.xlsx', index=False)
```

## Usage

1. Ensure you have the required Python library, **pandas**, installed.
2. Prepare an Excel file named **random_data.xlsx** containing the necessary data.
3. Call the **count_montecarlo()** function to calculate and save relative counts based on specified threshold values.

## Description

- The script loads data from an Excel file, **random_data.xlsx**.
- It calculates relative counts for a list of threshold values, ranging from 0.05 to 1.
- The relative count for each threshold is calculated as the count of PGA values greater than or equal to the threshold divided by the total number of rows in the data.
- The calculated relative counts are stored in a new DataFrame.
- The resulting DataFrame is saved to a new Excel file named **relative_pga_counts.xlsx**.

You can use this script to generate relative counts for different PGA threshold values in your data.
