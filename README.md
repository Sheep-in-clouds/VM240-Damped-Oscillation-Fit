# Damped Oscillation Fitting

This Python script fits a damped oscillation model to experimental data using curve fitting techniques provided by `scipy.optimize.curve_fit`. The damped oscillation model used in this script is defined by the function `damped_oscillation`.

## Usage

To use this script, follow these steps:

1. Ensure you have Python installed on your system.
2. Install the required libraries by running `pip install numpy scipy matplotlib`.
3. Prepare your experimental data in a text file, where each line contains two numbers separated by whitespace: the time (t) and the corresponding displacement (x).
4. Update the `filepath` variable in the `main` function to point to your data file.
5. Run the script using the command `python script_name.py`, where `script_name.py` is the name of the Python script containing the provided code.

## Description

- `damped_oscillation`: This function defines the damped oscillation model. It takes time `t` and five parameters `A`, `B`, `mu`, `lam`, and `Y`, representing the amplitude, phase, angular frequency, decay constant, and offset, respectively. It returns the displacement at time `t` according to the damped oscillation model.
- `read_data`: This function reads experimental data from a text file. It takes the file path as input and returns two NumPy arrays: `t_data` (time) and `x_data` (displacement).
- `fit_data`: This function fits the damped oscillation model to the experimental data. It takes the time and displacement data as input and returns the optimized parameters for the damped oscillation model.
- `main`: This is the main function of the script. It reads the experimental data, fits the damped oscillation model to the data, and plots the original data along with the fitted curve using Matplotlib.

## Requirements

- Python 3.x
- NumPy
- SciPy
- Matplotlib

## Example

Suppose you have experimental data stored in a file named `experiment_data.txt`. To fit the damped oscillation model to this data, you would run the script with `filepath = 'experiment_data.txt'`. After running the script, it will display a plot showing the original data points and the fitted curve representing the damped oscillation model.

For any questions or issues, please contact [author_name](mailto:author_email).
