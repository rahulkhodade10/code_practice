import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder. \
    master('local'). \
    appName("aaaa"). \
    getOrCreate()

columns = ["language", "users_count"]
data = [("Java", "20000"), ("Python", "100000"), ("Scala", "3000")]

rdd = spark.sparkContext.parallelize(data)
rdd1 = rdd.toDF()
rdd1.printSchema()
