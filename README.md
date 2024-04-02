# README

## Overview

This Python script demonstrates how to interact with a MySQL database using the `mysql-connector-python` library. It includes functions for creating a server connection, creating a database, executing SQL queries, and reading query results.

## Prerequisites

- Python 3.x installed on your system
- `mysql-connector-python` library installed (`pip install mysql-connector-python`)
- A MySQL server running on your system or accessible through a network

## Usage

1. Replace the `host_name`, `user_name`, `user_password`, and `db_name` variables in the script with your MySQL server's host name, your user name, your password, and the desired database name.

2. Run the script using a Python interpreter or by executing the script file.

3. The script will create a new database (if it doesn't already exist), create an "orders" table, insert sample data into the table, and execute various SQL queries to read and manipulate the data. Finally, it will print the data from the "orders" table in a pandas DataFrame format.

## Functions

- `create_server_connection`: Establishes a connection to a MySQL server.
- `create_database`: Creates a new database with the specified name.
- `create_db_connection`: Establishes a connection to a specific database within a MySQL server.
- `execute_query`: Executes an SQL query on a database and commits the changes.
- `create_orders_table`: Contains the SQL query to create a new table called "orders" with the specified columns and data types.
- `read_query`: Executes an SQL query and returns the first row of the result set.

## Limitations

- The script assumes that the MySQL server is running on the local machine. If your server is running on a different machine, you will need to update the `host_name` variable accordingly.

- The sample data inserted into the "orders" table is hardcoded. If you want to insert different data, you will need to modify the `data_orders` variable.

- The script only reads the first row of the result set when executing a query. If you need to read all the rows, you will need to modify the `read_query` function accordingly.
