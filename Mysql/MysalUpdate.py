import mysql.connector
from mysql.connector import Error
try:
  connection = mysql.connector.connect(host='localhost', user='root', password='root', database='test_db')

  cursor = connection.cursor()
  print("Before updating a record ")

  sql_select_query = "select * from users where user_id =1"
  cursor.execute(sql_select_query)
  record=cursor.fetchone()
  print(record)

#update
  sql_update_query = "UPDATE users set is_active = 1 where user_id =1 "
  cursor.execute(sql_update_query)
  print("Record Updated successfully ")
  print("After updating record ")

  cursor.execute(sql_select_query)
  record=cursor.fetchone()
  print(record)

except Error as e:
 print("Failed to update table record: {}".format(e))
finally:
        if connection.is_connected():
         connection.close()
         print("MySQL connection is closed")

