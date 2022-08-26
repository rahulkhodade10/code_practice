import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='test_db',
                                         user='root',
                                         password='root')

    sql_select_Query = "select * from users"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)

    print("\nPrinting each row")
    for row in records:
        print("user_id = ", row[0], )
        print("user_first_name = ", row[1])


except mysql.connector.Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if connection.is_connected():
        connection.close()
        cursor.close()
        print("MySQL connection is closed")
