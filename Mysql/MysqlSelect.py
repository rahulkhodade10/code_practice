import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost', user='root', password='root', database='test_db')
    sql_select_Query ="select * from laptop"
    cursor =connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)

    print("\nPrinting each row")
    for row in records:
        print("Id = ", row[0], )
        print("Name = ", row[1])
        print("Price  = ", row[2])
        print("Purchase date  = ", row[3], "\n")
except Error as e:
    print(format(e))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
    print("MySQL connection is closed")
