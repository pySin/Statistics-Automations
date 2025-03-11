from regression import Regression
from data_processing import ProcessData

x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y_values = [25, 38, 29, 115, 82, 114, 120, 160, 153, 190, 239, 175]


if __name__ == "__main__":
    database = "world"
    table = "country"
    numeric_columns = ["LifeExpectancy", "GNP", "GNPOld"]

    process_data = ProcessData(database, table, numeric_columns)
    column_combinations = process_data.columns_combinations()
    x, y, labels = process_data.process_data(["LifeExpectancy", "GNP"])

    regression_c = Regression()
    regression_c.slope_calculate(x, y)
    regression_c.regression_plot(labels)
    print(f"Column Combinations: {column_combinations}")


