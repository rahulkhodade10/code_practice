import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', password='root' ,db = 'test_db')

mycursor = mydb.cursor()
mycursor.execute('select * from users')

result = mycursor.fetchone()
for i in result:
    print(i)
