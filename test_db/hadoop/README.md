docker pull rkhomenko/greenplum

curl -XPOST http://172.18.0.10:7077/v1/submissions/create \
--header "Content-Type:application/json;charset=UTF-8" \
--data '{
  "appResource": "",
  "sparkProperties": {
    "spark.master": "spark://master:7077",
    "spark.app.name": "Spark Pi",
    "spark.driver.memory": "1g",
    "spark.driver.cores": "1",
    "spark.jars": ""
  },
  "clientSparkVersion": "",
  "mainClass": "org.apache.spark.deploy.SparkSubmit",
  "environmentVariables": { },
  "action": "CreateSubmissionRequest",
  "appArgs": [ "test_db/change_spark/src/get_data.py", "10" ]
}'


/spark/bin/pyspark --master "spark://spark-master:7077" "/test_db/src/get_data.py"