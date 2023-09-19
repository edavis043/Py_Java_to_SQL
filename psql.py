import os
import mysql.connector

db_username = os.environ.get('DB_USERNAME')
db_password = os.environ.get('DB_PASSWORD')
db_name = os.environ.get('DB_NAME')

with open('sums.txt', 'r') as file:
    lines = file.readlines()

calc_part = []  #It contains all calculations and its output.
total_Part = [] #It contain the total result and it's Desc.

for line in lines:
    parts = line.strip().split('=')
    if len(parts) == 2:
        calc = parts[0].strip()
        result = int(parts[1].strip())
        calc_part.append((calc, result))

    total = line.strip().split(':')
    if len(total) == 2:
        desc = total[0].strip()
        val = total[1].strip()
        total_Part.append((desc, val))

# print(calc_part)
# print(total_Part)

connection = mysql.connector.connect(
        user=db_username,
        password=db_password,
        host='localhost',
        database=db_name
    )

cursor = connection.cursor()

try:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS sum_data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        calculation VARCHAR(255),
        result INT
    )
    """
    cursor.execute(create_table_query)

    insert_query = "INSERT INTO sum_data (calculation, result) VALUES (%s, %s)"
    cursor.executemany(insert_query, calc_part)

    insert_query = "INSERT INTO sum_data (calculation, result) VALUES (%s, %s)"
    cursor.executemany(insert_query, total_Part)

    connection.commit()
    print("Data inserted successfully!")

except mysql.connector.Error as error:
    print(f"Error: {error}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
