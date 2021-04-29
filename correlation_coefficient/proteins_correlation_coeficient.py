# Proteins Correlation Coefficient

import mysql.connector
import re
import math


# Find the statistical Correlation Coeficient between every 2 columns
# with numeric data from a MySQL table.
class correlation_coeficient:

    def __init__(self, table_name):
        self.table_name = table_name

    # Get the table columns names. A string has to be constructed that
    # looks exactly like SQL query. This query is then sent to the MySQL
    # server and the result is assigned to a variable with fetchall()
    # function.
    def get_col_names(self):
        self.database = self.table_name.split('.')[0]  # Obtain database and
        self.table = self.table_name.split('.')[1]  # table names.

        get_c_names = '''
                  SELECT COLUMN_NAME
                  FROM INFORMATION_SCHEMA.COLUMNS
                  WHERE TABLE_SCHEMA = \'%s\'
                  AND
                  TABLE_NAME = \'%s\';
                      ''' % (self.database, self.table)

        conn = mysql.connector.connect(host='localhost', user='root',
                                       password='dance')  # MySQL connection.
        cursor = conn.cursor()
        cursor.execute(get_c_names)
        col_names = cursor.fetchall()

        # Transform the list from the fetchall() function to simple
        # list of strings.
        self.table_columns = [re.sub(r'\(|\)|\'|,', '', str(x))
                              for x in col_names]

        conn.commit()  # Send the query to MySQL.

    # Create a combination of every possible pair between the column names
    # excluding two identical names.
    def list_double_combination(self):

        self.double_comb = []

        for item in self.table_columns:
            for inner_item in self.table_columns:
                if inner_item == item:
                    continue
                self.double_comb.append([item, inner_item])

        return self.double_comb

    # Get the data from the 2 columns in a pair.
    def two_columns(self, column_1, column_2):

        query = '''
            SELECT %s, %s FROM %s;
                ''' % (column_1, column_2, self.table_name)

        conn = mysql.connector.connect(host='localhost', user='root',
                                       password='dance')  # MySQL connection.

        cursor = conn.cursor()
        cursor.execute(query)
        two_col_data = cursor.fetchall()

        # The data sent to python from MySQL is in tuples with 2 values each.
        # The first value is from the first MySQL column and the second value
        # from the second. We have to devide the pair anr reconstruct the
        # columns.
        column_1 = [x[0] for x in two_col_data]
        column_2 = [x[1] for x in two_col_data]
        conn.commit()
        return column_1, column_2

    # Create a table in MySQL for the data of the analysis with an 'id',
    # 'column_combination' and 'correlation' columns.
    def create_table(self):

        create_query = '''
    CREATE TABLE IF NOT EXISTS %s_correlation
                                (id INT AUTO_INCREMENT PRIMARY KEY,
                                column_combination VARCHAR(255),
                                correlation FLOAT(5, 4)
                                );
                       ''' % (self.table_name)

        conn = mysql.connector.connect(host='localhost', user='root',
                                       password='dance')  # MySQL connection.
        cursor = conn.cursor()
        cursor.execute(create_query)

        conn.commit()

    # Insert the calculated data with it's respective combination string.
    def insert_correlation_mysql(self, correlating_two, c_coefficient):

        query = '''
            INSERT INTO %s_correlation(column_combination, correlation)
            VALUES(\'%s\', %s);
                ''' % (self.table_name, correlating_two, c_coefficient)

        conn = mysql.connector.connect(host='localhost', user='root',
                                       password='dance')  # MySQL connection.
        cursor = conn.cursor()
        cursor.execute(query)

        conn.commit()


# Calculate the correlation coeficient.
class correlation_coef:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.n = len(x)

    # Find the statistical Standart Deviation for a column of numeric values.
    def st_dev(self, d_col):
        d_col_squares = [(i - (sum(d_col) / len(d_col)))**2 for i in d_col]
        sum_d_col_squares = round(sum(d_col_squares), 5)
        n_minus_1 = len(d_col) - 1
        st_dev = math.sqrt(sum_d_col_squares / n_minus_1)
        return st_dev

    # Find the 2 Standart Deviations for the each column in the comparrison
    # (x and y).
    def st_dev_xy(self):
        self.st_dev_x = self.st_dev(self.x)
        self.st_dev_y = self.st_dev(self.y)

    # Use the formula for Statistical Correlation Coeficient between 2 columns.
    # We need the mean and Standart Deviation for 'x' and 'y'. We already found
    # the Standart Deviations in the functions above.
    def corr(self):

        # Find the statistical mean for x-column and y-column.
        self.mean_x = sum(self.x) / len(self.x)
        self.mean_y = sum(self.y) / len(self.y)

        # Calculate the Correlation Coeficient trough it's formula('r').
        self.corr_co_xy_sum = []
        for item in range(0, len(self.x)):
            x_part = (self.x[item] - self.mean_x) / self.st_dev_x
            y_part = (self.y[item] - self.mean_y) / self.st_dev_y
            # print('X part =', x_part)
            # print('Y part', y_part)
            corr_c_xy = x_part*y_part
            self.corr_co_xy_sum.append(corr_c_xy)

        self.summation_part = sum(self.corr_co_xy_sum)
        r = ((1 / (self.n-1))*(self.summation_part))
        return r

    # Call the functions to create the variables needed for the Correlation
    # Coeficient formula.
    def show_correlation(self):
        self.st_dev(self.x)
        self.st_dev_xy()
        return self.corr()


# Functions call.
def call_functions():

    correlation_c = correlation_coeficient('world_2.country_x')
    correlation_c.get_col_names()
    correlation_c.create_table()
    double_combinations = correlation_c.list_double_combination()

    # Get the data from each pair of columns and calculate their correlation.
    # Add the column combination name and the Correlation Coeficient in a new
    # MySQL table.
    for item in double_combinations:
        column_1, column_2 = correlation_c.two_columns(item[0], item[1])

        correlation_calc = correlation_coef(column_1, column_2)
        r = correlation_calc.show_correlation()
        combination_name = item[0]+'-'+item[1]
        correlation_c.insert_correlation_mysql(combination_name, r)


if __name__ == '__main__':
    call_functions()
