import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='mydatabase'
)

mycursor = mydb.cursor()

# 1) create database
# mycursor.execute("CREATE DATABASE mydatabase")

# 2)Check if Database Exists

mycursor.execute('show databases')
for i in mycursor:
    print(i)

# 3) Create table

#mycursor.execute('CREATE TABLE customers (name VARCHAR(20), address VARCHAR(255))')

# 4)Check if Table Exists

mycursor.execute('SHOW TABLES')
for i in mycursor:
    print(i)

