from pyspark import SparkContext
from pyspark.sql import SparkSession


def main():
    spark = (SparkSession.builder.appName("MySparkApp").getOrCreate())
    brewfile = spark.write.csv("hdfs://namenode:9000/data/openbeer/breweries/breweries.csv")
    brewfile.show()
    spark.stop()


if __name__ == "__main__":
    main()
