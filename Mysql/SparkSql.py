import mysql.connector
import pandas as pd
from pyspark.sql import SparkSession

appName = "PySpark MySQL Example - via mysql.connector"
master = "local"

spark = SparkSession.builder.master(master).appName(appName).getOrCreate()

# Establish a connection
conn = mysql.connector.connect(user='root', database='test_db',
                               password='root',
                               host="localhost",
                               port=3306
                               )
cursor = conn.cursor()
query = "SELECT * from users"
# Create a pandas dataframe
pdf = pd.read_sql(query, con=conn)
conn.close()
print(pdf.head())