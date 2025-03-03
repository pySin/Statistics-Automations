# Regression
from curses.ascii import isdigit


class Regression:

    def __init__(self):
        self.x_values_iv = None
        self.y_values_dv = None

    @staticmethod
    def receive_data(x_values_iv, y_values_dv):
        if len(x_values_iv) != len(y_values_dv):
            raise ValueError("The amount of x values has to be the same as the amount of y values!")

        if not all(map(isdigit, x_values_iv)):
            raise ValueError("All x values has to be numeric!")


    def slope_calculate(self):
        x_mean = sum(self.x_values_iv) / len(self.x_values_iv)
        y_mean = sum(self.y_values_dv) / len(self.y_values_dv)
        print(f"X mean: {x_mean}")
        print(f"Y mean: {y_mean}")

        xy_summation = 0
        x_2_summation = 0
        for i in range(len(self.x_values_iv)):
            xy_summation += (self.x_values_iv[i] - x_mean) * (self.y_values_dv[i] - y_mean)
            x_2_summation += (self.x_values_iv[i] - x_mean) ** 2

        slope = xy_summation / x_2_summation
        print(f"Slope: {slope}")

