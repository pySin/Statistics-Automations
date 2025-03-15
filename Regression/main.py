from regression import Regression
from data_processing import ProcessData


def caller():
    database = "world"
    table = "country"
    numeric_columns = ["LifeExpectancy", "GNP", "GNPOld", "SurfaceArea", "Population"]
    # category_columns = None  # A project for the category columns comparison

    process_data = ProcessData(database, table, numeric_columns)
    column_combinations = process_data.columns_combinations()

    for current_combination in column_combinations:
        print(f"Current Combination: {current_combination}")
        x, y, labels = process_data.process_data(current_combination)

        regression_c = Regression()
        regression_c.slope_calculate(x, y)
        if regression_c.slope_significance():
            regression_c.regression_plot(labels, current_combination, database, table)
        else:
            print(f"Slope does not have statistical significance!")


if __name__ == "__main__":
    caller()

