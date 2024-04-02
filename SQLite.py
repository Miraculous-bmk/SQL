import mysql.connector
from mysql.connector import Error
import  pandas as pd

def create_server_connection(host_name,user_name,user_password):
    Connection = None
    try:
        Connection = mysql.connector.connect(
            host= host_name,
            user= user_name,
            passwd= user_password)
        print("MySQL Database connection established")
    except Error as err:
        print(f"Error: '{err}.message'")
    return Connection
#put our MySQL Terminal password
pw = "5565585Mira@"

#Database name
db ="mysql_python"
connection = create_server_connection("localhost","root", pw)

#create mysql_python
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")
create_database_query= "create_database mysql_python"
create_database(connection, create_database_query)

#connect to database
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host_name = host_name,
            user_name = user_name,
            passwd = user_password,
            database = db_name)
    except Error as err:
        print(f"Error: '{err}'")
    return connection

#Execute the sql query
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        cursor= connection.commit()
        print("Query was successfully")
    except Error as err:
        print(f"Error: '{err}'")

#Create orders table
create_orders_table= """
    create order table(
        order_id int primary key,
        customer_name varchar(30) not null,
        product_name varchar(20) not null,
        date_ordered date,
        quantity int,
        unit_price float,
        phone_number varchar(20))
    """
#connect to the database
connection= create_db_connection("localhost", "root", pw, db)
execute_query(connection, create_orders_table)

#insert data
data_orders = """
insert into orders values
(101, 'Steve', 'laptop', '2018-6-12', 2, 800, '6293730802'),
(102, 'Jos', 'Books', '2019-2-10', 10, 12, '8367489124'),
(103, 'Stacy', 'Trousers', '2019-12-25', 5, 50, '8976123645'),
(104, 'Nancy', 'T-shirts', '2018-7-4', 7, 30, '7368145099'),
(105, 'Maria, 'Headphones', '2019-05-30', 6, 48, '8865316698'),
(106, 'Danny', 'Smart TV', '2018-08-20', 10, 300, '7720130446');
"""
connection = create_db_connection("localhost","root", pw, db)
execute_query(connection, create_orders_table)

def read_query(connection, query):
    cursor =connection.curser()
    result =None
    try:
        cursor.execute(query)
        result =cursor.fetchone()
        return result
    except Error as err:
        print(f"Error: '{err}'")

#using the select start
q1 = """select + from orders;"""
connection = create_db_connection("localhost","root", pw, db)
results= read_query(connection, q1)
for result in results:
    print(result)

q2 = """select customer_name, phone_number from orders;"""
connection = create_db_connection("localhost","root", pw, db)
results= read_query(connection, q2)
for result in results:
    print(result)

q3 = """select year(data_ordered) from orders;"""
connection = create_db_connection("localhost","root", pw, db)
results= read_query(connection, q3)
for result in results:
    print(result)

q4 = """select distinct year(data_ordered) from orders;"""
connection = create_db_connection("localhost","root", pw, db)
results= read_query(connection, q4)
for result in results:
    print(result)

q5= """select + from orders where data_ordered < '2018-12-31';"""
connection = create_db_connection("localhost","root", pw, db)
results= read_query(connection, q5)
for result in results:
    print(result)

q6= """select + from orders where data_ordered > '2018-12-31';"""
connection = create_db_connection("localhost","root", pw, db)
results= read_query(connection, q6)
for result in results:
    print(result)

q7= """select + from orders order by unit_price desc;"""
connection = create_db_connection("localhost","root", pw, db)
results= read_query(connection, q7)
for result in results:
    print(result)

from_db =[]
for result in results:
    result = list(result)
    from_db.append(result)
columns = ["order_id", "customer_name", "product_name", "date_ordered", "quantity",
           "unit_price", "phone_number"]
df = pd.DataFrame(from_db, columns=columns)
print(df)
