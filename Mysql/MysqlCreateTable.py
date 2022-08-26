import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost', user='root', password='root', database='test_db')

    mysql_createTable = """CREATE TABLE laptop(
                         id INT(11) NOT NULL,
                         name VARCHAR(20) NOT NULL,
                         price FLOAT NOT NULL,
                         purchase_date Date NOT NULL,
                         PRIMARY KEY (id))"""

    cursor = connection.cursor()
    result=cursor.execute(mysql_createTable)
    cursor = connection.cursor()
    cursor.execute("select database();")
    print("Laptop Table created successfully ")

except Error as e:
    print("Failed to create table in MySQL: {}".format(e))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


