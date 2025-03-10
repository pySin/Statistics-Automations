import numpy as np

# Independent variable (x)
x = np.array([39.52, 44.15, 48.78, 53.41, 58.03, 62.67, 67.3, 71.93, 76.56, 81.19])

# Dependent variable (y)
y = np.array([3370.67, 3907.8, 2711.93, 35223.27, 7908.08, 72312.35, 33119.75, 54662.36, 354563.17, 512215.15])

# Add a column of ones for the intercept
A = np.vstack([x, np.ones(len(x))]).T
print(A)

from scipy.optimize import nnls

# Fit the model using NNLS
coefficients, _ = nnls(A, y)
print(f"Coefficients Zero: {coefficients}, {_}")

# Extract the slope and intercept
slope = coefficients[0]
intercept = coefficients[1]

print(f"Slope: {slope}")
print(f"Intercept: {intercept}")

# Calculate predicted y values
y_pred = slope * x + intercept

import matplotlib.pyplot as plt

# Plot the data points
plt.scatter(x, y, color='blue', label='Data Points')

# Plot the regression line
plt.plot(x, y_pred, color='red', label=f'Regression Line: y = {intercept:.2f} + {slope:.2f}x')

# Add labels and title
plt.xlabel('Independent Variable (x)')
plt.ylabel('Dependent Variable (y)')
plt.title('Regression Line with Non-Negative Intercept')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()

