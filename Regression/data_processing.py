# Data Processing
import mysql.connector


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
        print(f"List Data: {data_list}")
        print(f"List Data Length: {len(data_list)}")
        return data_list

    def clear_outliers(self):
        x_y_data = self.data_clear_zero_null()

def caller():
    numeric_cols = ["LifeExpectancy", "GNP", "GNPOld"]
    process_data = ProcessData("world", "country", numeric_cols)
    process_data.columns_combinations()
    rd = process_data.get_raw_col_data(["LifeExpectancy", "GNP"])
    process_data.data_clear_zero_null(rd)


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
