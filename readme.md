# Monte Carlo Simulation for Ground Motion Prediction

This repository contains a Python script that performs a Monte Carlo simulation for predicting ground motion using the Gutenberg-Richter law and the AmberSIS empirical ground motion prediction equation. The generated data is stored in an Excel file and can be used for seismic hazard analysis and risk assessment.

## Getting Started

These instructions will help you set up and run the Monte Carlo simulation on your local machine.

### Prerequisites

Before running the code, make sure you have the following libraries installed:

- `random`: For generating random numbers.
- `math`: For mathematical operations.
- `pandas`: For data manipulation and storage.
- `numpy` for mathematical operations.
- `matplotlib.pyplot` for data visualization.

### Installation

To install the required libraries, you can use `pip`:

```bash
pip install pandas numpy matplotlib
```


**Parameters and Constants**

```markdown
## Parameters and Constants

The following parameters and constants are used in the simulation:

- `M_min`: Minimum magnitude (earthquake magnitude).
- `M_max`: Maximum magnitude.
- `R_min`: Minimum distance.
- `R_max`: Maximum distance.
- `iterate`: Number of iterations for data generation.


**Running the Simulation**

```markdown
### Running the Simulation

To run the Monte Carlo simulation, simply execute the provided script, main.py`.

```bash
python main.py
```
