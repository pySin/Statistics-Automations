# Regression
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class Regression:

    def __init__(self):
        self.x_values_iv = None
        self.y_values_dv = None

    @staticmethod
    def check_digit(num):
        try:
            check_num = num + 1
        except TypeError:
            return False
        return True

    def receive_data(self, x_values_iv, y_values_dv):
        if len(x_values_iv) != len(y_values_dv):
            raise ValueError("The amount of x values has to be the same as the amount of y values!")

        if not all(map(self.check_digit, x_values_iv)):
            raise ValueError("All x values has to be numeric!")

        if not all(map(self.check_digit, y_values_dv)):
            raise ValueError("All y values has to be numeric!")

        if type(x_values_iv) != list or type(y_values_dv) != list:
            raise TypeError("All independent and dependent values(x, y) must be in a list!")

        self.x_values_iv = x_values_iv
        self.y_values_dv = y_values_dv


    def slope_calculate(self, x_values_iv, y_values_dv):
        self.receive_data(x_values_iv, y_values_dv)

        x_mean = sum(self.x_values_iv) / len(self.x_values_iv)
        y_mean = sum(self.y_values_dv) / len(self.y_values_dv)
        print(f"X mean: {x_mean}")
        print(f"Y mean: {y_mean}")

        xy_summation = 0
        x_2_summation = 0
        print(f"X values iv: {x_values_iv}")
        print(f"Y values dv: {y_values_dv}")
        for i in range(len(self.x_values_iv)):
            xy_summation += (self.x_values_iv[i] - x_mean) * (self.y_values_dv[i] - y_mean)
            x_2_summation += (self.x_values_iv[i] - x_mean) ** 2
        print(f"XY summation: {xy_summation}")
        print(f"X_2 summation: {x_2_summation}")

        slope = xy_summation / x_2_summation
        print(f"Slope: {slope}")
        return slope

    def intercept_calculate(self, x_values_iv, y_values_dv):
        x_mean = sum(self.x_values_iv) / len(self.x_values_iv)
        y_mean = sum(self.y_values_dv) / len(self.y_values_dv)

        slope = self.slope_calculate(x_values_iv, y_values_dv)

        intercept_xy = y_mean - (slope * x_mean)
        print(f"Intercept: {intercept_xy}")
        return intercept_xy

    def slope_significance(self):
        slope = self.slope_calculate(self.x_values_iv, self.y_values_dv)
        intercept = self.intercept_calculate(self.x_values_iv, self.y_values_dv)
        residuals = 0

        for i in range(len(self.y_values_dv)):
            residuals += (self.y_values_dv[i] - (intercept + slope * self.x_values_iv[i])) ** 2

        x_squared_summation = 0

        for cx in self.x_values_iv:
            x_squared_summation += cx ** 2






    def regression_plot(self, x_labels, column_combination, database, table):
        intercept_xy = self.intercept_calculate(self.x_values_iv, self.y_values_dv)
        slope = self.slope_calculate(self.x_values_iv, self.y_values_dv)
        y_on_regression_line = [intercept_xy + (slope * x) for x in self.x_values_iv]

        # Create the regression plot
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=self.x_values_iv, y=self.y_values_dv, color='blue', label='Data Points')  # Plot data points
        plt.plot(self.x_values_iv, y_on_regression_line, color='red',
                 label=f'Regression Line: y = {intercept_xy:.2f} + {slope:.2f}x')  # Plot regression line

        # Add adjusted x-labels
        plt.xticks(self.x_values_iv, x_labels, fontsize=8, rotation=45, ha="right")

        # Add labels and title
        x_column = column_combination[0]
        plt.xlabel(x_column)
        y_column = column_combination[1]
        plt.ylabel(y_column)

        plt.title(f'{database} {table}'.title())
        plt.legend()
        plt.grid(True)

        # Show the plot
        # plt.show()

        # Find longest label
        longest_label = max([len(l) for l in x_labels])

        # Increase bottom margin
        plt.subplots_adjust(bottom=(longest_label / 100) + 0.05)

        # Save plot
        plt.savefig(f"plots/{x_column} - {y_column}.png")

