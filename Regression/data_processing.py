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
        print(f"Column Combinations: {col_combinations}")
        return col_combinations


def caller():
    numeric_cols = ["LifeExpectancy", "GNP", "GNPOld"]
    process_data = ProcessData("world", "country", numeric_cols)
    process_data.columns_combinations()


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
