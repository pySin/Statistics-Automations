import numpy as np

# Independent variable (x)
x = np.array([39.52, 44.15, 48.78, 53.41, 58.03, 62.67, 67.3, 71.93, 76.56, 81.19])

# Dependent variable (y)
y = np.array([3370.67, 3907.8, 2711.93, 35223.27, 7908.08, 72312.35, 33119.75, 54662.36, 354563.17, 512215.15])

# Add a column of ones for the intercept
A = np.vstack([x, np.ones(len(x))]).T
print(A)
