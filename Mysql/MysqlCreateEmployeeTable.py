import mysql.connector
from mysql.connector import Error

try:

    connection =mysql.connector.connect(host='localhost',user='root', password='root',database='test_db')
    mysql_createTable= """CREATE TABLE employee (empno INT,
                         ename VARCHAR(100),
                        designation VARCHAR(100),
                        manager INT,
                        hire_date VARCHAR(50),
                        sal INT,
                         deptno INT)"""
    cursor=connection.cursor()
    cursor.execute(mysql_createTable)
    print('Employee table create successfully')

except Error as e:
    print("Failed to create table in MySQL: {}".format(e))

finally:
    if connection.is_connected():
        connection.close()
        cursor.close()
        print("Database exit")