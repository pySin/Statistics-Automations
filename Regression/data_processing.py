# Data Processing

import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root',
                               password='dance')  # MySQL connection.

independent_var = "LifeExpectancy"
dependent_var = "GNP"

query = "SELECT LifeExpectancy, GNP FROM world.country;"

cursor = conn.cursor()
cursor.execute(query)
results = cursor.fetchall()

for result in results:
    print(f"Result: {result[0]}")

print(f"Results: {results}")
