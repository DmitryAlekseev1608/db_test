from pyspark.sql import SparkSession
from src.constants import GREENPLUM
import logging


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s:%(funcName)s:%(levelname)s:%(message)s"
)


def create_spark_session() -> SparkSession:
    spark = (
        SparkSession
        .builder
        .appName("GreenPlum Connection with PySpark")
        .config(
            "spark.jars.packages",
            "org.postgresql:postgresql:42.7.4",
        )
        .getOrCreate()
    )

    logging.info("Spark session created successfully")
    return spark


def get_data_from_gp(spark):
    existing_data_df = spark.read.jdbc(
        GREENPLUM.URL, "employ", properties=GREENPLUM.PROPERTIES
    )
    existing_data_df.show()
    spark.close()


def write_to_postgres():
    spark = create_spark_session()
    df = get_data_from_gp(spark)