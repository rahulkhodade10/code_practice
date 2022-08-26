def from_files(spark):
    df = spark.read.format("jdbc"). \
        option("url", "jdbc:mysql://localhost:3306/testdb"). \
        option("driver", "com.mysql.jdbc.Driver"). \
        option("dbtable", "books"). \
        option("user", "root"). \
        option("password", "root"). \
        load()

    return df
