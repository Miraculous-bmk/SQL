import mysql.connector
from mysql.connector import Error
import pandas as pd

def create_server_connection(host_name, user_name, user_password):
    Connection = None
    try:
        Connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password)
        print("MySQL Database connection established")
    except Error as err:
        print(f"Error: '{err}'.message")
    return Connection

# put our MySQL Terminal password
pw = "add your own password"

# Database name
db = "mysql_python"
connection = create_server_connection("localhost", "root", pw)

# create mysql_python
def create_database(connection, query):
    """Creates a database using the provided connection and query."""
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

create_database_query = "CREATE DATABASE IF NOT EXISTS mysql_python"
create_database(connection, create_database_query)

# connect to database
def create_db_connection(host_name, user_name, user_password, db_name):
    """Establishes a connection to a specific database."""
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name)
    except Error as err:
        print(f"Error: '{err}'")
    return connection

# Execute the sql query
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query was successful")
    except Error as err:
        print(f"Error: '{err}'")

# Create orders table
create_orders_table = """
    CREATE TABLE IF NOT EXISTS orders (
        order_id INT PRIMARY KEY,
        customer_name VARCHAR(30) NOT NULL,
        product_name VARCHAR(20) NOT NULL,
        date_ordered DATE,
        quantity INT,
        unit_price FLOAT,
        phone_number VARCHAR(20)
    )
"""

# connect to the database
connection = create_db_connection("localhost", "root", pw, db)
execute_query(connection, create_orders_table)

# insert data
data_orders = """
INSERT INTO orders VALUES
(101, 'Steve', 'laptop', '2018-06-12', 2, 800, '6293730802'),
(102, 'Jos', 'Books', '2019-02-10', 10, 12, '8367489124'),
(103, 'Stacy', 'Trousers', '2019-12-25', 5, 50, '8976123645'),
(104, 'Nancy', 'T-shirts', '2018-07-04', 7, 30, '7368145099'),
(105, 'Maria', 'Headphones', '2019-05-30', 6, 48, '8865316698'),
(106, 'Danny', 'Smart TV', '2018-08-20', 10, 300, '7720130446')
"""

execute_query(connection, data_orders)

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

# using the select start
q1 = """SELECT * FROM orders"""
results = read_query(connection, q1)
for result in results:
    print(result)

q2 = """SELECT customer_name, phone_number FROM orders"""
results = read_query(connection, q2)
for result in results:
    print(result)

q3 = """SELECT YEAR(date_ordered) FROM orders"""
results = read_query(connection, q3)
for result in results:
    print(result)

q4 = """SELECT DISTINCT YEAR(date_ordered) FROM orders"""
results = read_query(connection, q4)
for result in results:
    print(result)

q5 = """SELECT * FROM orders WHERE date_ordered < '2018-12-31'"""
results = read_query(connection, q5)
for result in results:
    print(result)

q6 = """SELECT * FROM orders WHERE date_ordered > '2018-12-31'"""
results = read_query(connection, q6)
for result in results:
    print(result)

q7 = """SELECT * FROM orders ORDER BY unit_price DESC"""
results = read_query(connection, q7)
for result in results:
    print(result)

# Fetch tables
def fetch_tables(connection):
    query = "SHOW TABLES"
    tables = read_query(connection, query)
    table_names = [table[0] for table in tables]
    return table_names

print("Tables in the database:")
tables = fetch_tables(connection)
for table in tables:
    print(table)

from_db = []
for result in results:
    result = list(result)
    from_db.append(result)

columns = ["order_id", "customer_name", "product_name", "date_ordered", "quantity",
           "unit_price", "phone_number"]
df = pd.DataFrame(from_db, columns=columns)
print(df)

# Now let's close the connection
if connection.is_connected():
    connection.close()
    print("MySQL Database connection closed")
