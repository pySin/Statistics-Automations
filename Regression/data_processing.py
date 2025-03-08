# Data Processing
import mysql.connector
import math


class ProcessData:

    def __init__(self, database: str, table: str, numeric_columns: list):
        self.conn = mysql.connector.connect(host='localhost', user='root',
                                       password='dance')  # MySQL connection.
        self.database = database
        self.table = table
        self.numeric_columns = numeric_columns

    def columns_combinations(self):

        col_combinations = []

        for col in self.numeric_columns:
            for col_s in self.numeric_columns:
                if col != col_s and [col, col_s] not in col_combinations:
                    col_combinations.append([col, col_s])
        return col_combinations

    def get_raw_col_data(self, col_combination: list):
        independent_var = col_combination[0]
        dependent_var = col_combination[1]

        query = f"SELECT {independent_var}, {dependent_var} FROM {self.database}.{self.table};"

        cursor = self.conn.cursor()
        cursor.execute(query)
        raw_data = cursor.fetchall()
        return raw_data


    @staticmethod
    def data_clear_zero_null(raw_data: list):

        data_list = []

        for row in raw_data:
            try:
                data_list.append([float(row[0]), float(row[1])])
            except Exception:
                pass

        data_list = [d for d in data_list if d[0] != 0 and d[1] != 0]
        return data_list

    @staticmethod
    def clear_outliers(no_null_zero_data):

        # Find Standard deviation for X
        independent_val_x = [x[0] for x in no_null_zero_data]
        x_mean = sum(independent_val_x) / len(independent_val_x)
        x_summation = 0

        for x_val in independent_val_x:
            x_summation += (x_val - x_mean) ** 2

        standard_deviation_x = math.sqrt(x_summation / len(independent_val_x))

        # Find Standard deviation for Y
        independent_val_y = [y[1] for y in no_null_zero_data]
        y_mean = sum(independent_val_y) / len(independent_val_y)
        y_summation = 0

        for y_val in independent_val_y:
            y_summation += (y_val - y_mean) ** 2

        standard_deviation_y = math.sqrt(y_summation / len(independent_val_y))

        no_null_zero_data = [cd for cd in no_null_zero_data
                             if
                             (x_mean - (3 * standard_deviation_x)) < cd[0] < (x_mean + (3 * standard_deviation_x))
                             and
                             (y_mean - (3 * standard_deviation_y)) < cd[0] < (y_mean + (3 * standard_deviation_y))]
        return no_null_zero_data

    @staticmethod
    def x_bins_y_mean(clear_data):

        max_x = max([x[0] for x in clear_data])
        min_x = min([x[0] for x in clear_data])
        x_range = max_x - min_x
        bin_range = x_range / 10

        x_bins_y_values = []

        for v in clear_data:
            for i in range(10):
                if min_x + (i * bin_range) <= v[0] < min_x + (bin_range * (i + 1)):
                    x_bins_y_values.append([[min_x + (i * bin_range), min_x + (bin_range * (i + 1))], [v[1]]])

        x_bins_y_set = []

        for xy in x_bins_y_values:
            if xy[0] in [xs[0] for xs in x_bins_y_set]:
                for xi in range(len(x_bins_y_set)):
                    if x_bins_y_set[xi][0] == xy[0]:
                        x_bins_y_set[xi][1].append(xy[1][0])
            else:
                x_bins_y_set.append(xy)


        labels = [str([round(xb[0][0], 2), round(xb[0][1], 2)])[1:-1].replace(", ", " - ") for xb in x_bins_y_set]

        x_y = [[round(sum(xy_v[0]) / len(xy_v[0]), 2), round(sum(xy_v[1]) / len(xy_v[1]), 2)] for xy_v in x_bins_y_set]
        x_y = sorted(x_y, key=lambda x: x[0])
        x = [xy[0] for xy in x_y]
        y = [xy[1] for xy in x_y]

        return x, y, labels

    def process_data(self, column_pair: list):
        raw_data = self.get_raw_col_data(column_pair)
        no_null_zero_data = self.data_clear_zero_null(raw_data)
        no_outliers_data = self.clear_outliers(no_null_zero_data)
        x, y, labels = self.x_bins_y_mean(no_outliers_data)
        print(f"Labels_PD: {x, y, labels}")
        return x, y, labels





def caller():
    numeric_cols = ["LifeExpectancy", "GNP", "GNPOld"]
    process_data = ProcessData("world", "country", numeric_cols)
    process_data.columns_combinations()
    # raw_data = process_data.get_raw_col_data(["LifeExpectancy", "GNP"])
    # no_nz_data = process_data.data_clear_zero_null(raw_data)
    # no_outliers_data = process_data.clear_outliers(no_nz_data)
    # x_bins_y = process_data.x_bins_y_mean(no_outliers_data)
    # print(x_bins_y)
    process_data.process_data(["LifeExpectancy", "GNP"])


if __name__ == "__main__":
    caller()


# independent_var = "LifeExpectancy"
# dependent_var = "GNP"
#
# query = "SELECT LifeExpectancy, GNP FROM world.country;"
#
# cursor = conn.cursor()
# cursor.execute(query)
# results = cursor.fetchall()
#
# for result in results:
#     print(f"Result: {result[0]}")
#
# print(f"Results: {results}")
