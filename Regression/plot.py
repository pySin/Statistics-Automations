import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Provided data
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])  # Independent variable
y = np.array([25, 38, 29, 115, 82, 114, 120, 160, 153, 190, 239, 175])  # Dependent variable

# Reshape x to 2D array (required for scikit-learn)
x = x.reshape(-1, 1)

# Fit the regression model
model = LinearRegression()
model.fit(x, y)

# Get the slope and intercept
slope = model.coef_[0]
intercept = model.intercept_

# Predict y values for the regression line
y_pred = model.predict(x)
print(f"Y values: {y_pred}")

# Create the regression plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x=x.flatten(), y=y, color='blue', label='Data Points')  # Plot data points
plt.plot(x, y_pred, color='red', label=f'Regression Line: y = {intercept:.2f} + {slope:.2f}x')  # Plot regression line

# Add labels and title
plt.xlabel('Independent Variable (x)')
plt.ylabel('Dependent Variable (y)')
plt.title('Regression Plot')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()