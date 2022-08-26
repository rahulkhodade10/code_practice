import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost', user='root', password='root', database='test_db')
    mysql_insert_query= """INSERT INTO employee (empno, ename, designation, manager, hire_date, sal, deptno)
    VALUES (7369,'SMITH','CLERK',7902,'1980-12-17',800.00,20),
    (7499,'ALLEN','SALESMAN',7698,'1981-02-20',1600.00,30),
    (7521,'WARD','SALESMAN',7698,'1981-02-22',1250.00,30),
    (7566,'JONES','MANAGER',7839,'1981-04-02',2975.00,20),
    (7654,'MARTIN','SALESMAN',7698,'1981-09-28',1250.00,30)"""

    cursor=connection.cursor()
    cursor.execute(mysql_insert_query)
    connection.commit()
    cursor.close()
    print("Emoloyee insert query succesfull")

except Error as e:
    print("Failed to create table in MySQL: {}".format(e))

finally:
  connection.close()
  cursor.close()
  print('database exist')



