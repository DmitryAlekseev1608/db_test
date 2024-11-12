docker pull datagrip/greenplum
docker run datagrip/greenplum
apt update
apt install postgresql-client
psql -h localhost -U default -d default -p 5432

POSTGRES_JAR=$(ls /driver/postgresql-42.7.4.jar)
/spark/bin/spark-shell --jars "$${POSTGRES_JAR}" --driver-class-path ${POSTGRES_JAR}
