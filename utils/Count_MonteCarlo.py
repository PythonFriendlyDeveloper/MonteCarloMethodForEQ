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
