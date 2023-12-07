# Seismic Data Generation and Analysis

This Python script generates seismic data based on a Gutenberg-Richter distribution and performs Monte Carlo analysis. The generated data is saved to an Excel file for further analysis.

## Dependencies

- [random](https://docs.python.org/3/library/random.html): For generating random numbers.
- [math](https://docs.python.org/3/library/math.html): For mathematical operations.
- [pandas](https://pandas.pydata.org/): For data manipulation.
- `Count_MonteCarlo` and `Draw_MonteCarlo` from the `utils` package: Custom modules for Monte Carlo analysis.
- `Gutenberg_Richter` from the `utils` package: A custom module for Gutenberg-Richter distribution calculations.

Please ensure that you have these dependencies installed and accessible.

## Code

```python
# Import necessary libraries
import random
import math
import pandas as pd
from utils import Count_MonteCarlo, Draw_MonteCarlo
from utils import Gutenberg_Richter

# Number of iterations for data generation
iterate = 1000000

a, b, unique_magnitudes, log_counts, min_magnitude, max_magnitude = Gutenberg_Richter.gutenberg_richter_coefficients()
lambeda = 0

# Define parameters and constants
M_min = min_magnitude
M_max = max_magnitude
R_min = 0
R_max = 100
# Calculate N_min and N_max based on M_min and M_max
N_min = 10 ** (a - b * M_min)
N_max = 10 ** (a - b * M_max)

# Calculate P_min and P_max based on N_min and N_max
P_min = 1 - math.exp(-N_min)
P_max = 1 - math.exp(-N_max)

# Create empty lists to store data
M_random_data = []
R_random_data = []
sigma_inner_random_data = []
sigma_outer_random_data = []
lambeda_random_data = []
equation_data = []

# Function to calculate PGA values
def ambersis_PGA(M_random):
    PGA = [0, 2.522, -0.142, -3.184, 0.314, 7.6, 0.137, 0.050, -0.084, 0.062, -0.044, 0.665 - 0.065 * M_random, 0.222 - 0.022 * M_random]
    return PGA

# Define some constants
Ss = 1
SA = 0
FN = 0
FT = 0
F0 = 1

# Generate data in a loop
for i in range(iterate):
    lambeda = random.uniform(0, 1)
    if P_max < lambeda < P_min:
        N_random = -math.log(1 - lambeda)
        M_random = (a - math.log10(N_random)) / b
        R_random = random.uniform(R_min, R_max)
        sigma_number_inner = random.gauss(0, 1)
        sigma_number_outer = random.gauss(0, 1)
        PGA = ambersis_PGA(M_random)
        equation = PGA[1] + PGA[2] * M_random + (PGA[3] + PGA[4] * M_random) * math.log(math.sqrt(PGA[5] ** 2 + R_random ** 2)) + PGA[6] * Ss + PGA[7] * SA + PGA[8] * FN + PGA[9] * FT + PGA[10] * F0 + PGA[11] * sigma_number_inner + PGA[12] * sigma_number_outer
        equation = math.exp(equation)
        # Append data to respective lists
        M_random_data.append(M_random)
        R_random_data.append(R_random)
        sigma_inner_random_data.append(sigma_number_inner)
        sigma_outer_random_data.append(sigma_number_outer)
        lambeda_random_data.append(lambeda)
        equation_data.append(equation)

# Create a DataFrame to store the data
data = pd.DataFrame({'lambeda': lambeda_random_data, 'M_random': M_random_data, 'R_random': R_random_data, 'Sigma_outer': sigma_outer_random_data, 'Sigma_inner': sigma_inner_random_data, 'PGA': equation_data})

# Save the DataFrame to an Excel file
data.to_excel('utils/result/random_data.xlsx', index=False)
Count_MonteCarlo.count_montecarlo()
Draw_MonteCarlo.draw_montecarlo()
```

## Parameter Descriptions

- **iterate**: Number of iterations for data generation.
- **a, b, unique_magnitudes, log_counts, min_magnitude, max_magnitude**: Results from the Gutenberg-Richter distribution calculation.
- **M_min, M_max**: Minimum and maximum magnitude values.
- **R_min, R_max**: Minimum and maximum radius values.
- **N_min, N_max**: Calculated based on M_min and M_max.
- **P_min, P_max**: Calculated based on N_min and N_max.

Other parameters and constants, such as the function `ambersis_PGA`, and various factors used in data generation are also defined and used in the script.

This script generates seismic data based on a statistical distribution and performs Monte Carlo analysis. The generated data is saved for further analysis.
