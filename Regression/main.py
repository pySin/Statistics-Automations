from regression import Regression
from data_processing import ProcessData

x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y_values = [25, 38, 29, 115, 82, 114, 120, 160, 153, 190, 239, 175]


if __name__ == "__main__":


    regression_c = Regression()
    regression_c.slope_calculate(x_values, y_values)
    regression_c.regression_plot()


