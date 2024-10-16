# import findspark
# findspark.init('spark-2.4.1-bin-hadoop2.7')
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

option = {
    'url':"jdbc:postgresql://localhost:5432/tutorial",
    'user':"default",
    'password':"default",
    'dbschema':"default",
    'dbtable':"tourneys",
    'partitionColumn':"name"
}

gpdf = spark.read.format('io.pivotal.greenplum.spark.GreenplumRelationProvider').options(**option).load()
print(gpdf)