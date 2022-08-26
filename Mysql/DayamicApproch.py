import mysql.connector
import pandas as pd

with mysql.connector.connect(user='root', password='root', port=3306, database='test_db') as conn:
    with conn.cursor() as cursor:
        cursor.execute("""select * from information_schema.columns where table_name='laptop' """)
        cursor.execute("""desc customers""")

        conn.close()
