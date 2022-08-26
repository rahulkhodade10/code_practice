import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost', user='root', password='root', database='test_db')
    cursor = connection.cursor()

    print("before deleting record")
    sql_select_query = "select * from users"
    cursor.execute(sql_select_query)
    record = cursor.fetchall()
    print(record)

except Error as e:
    print(e)

finally:
    cursor.close()
    connection.close()

    print('Mysql connection is closed')
