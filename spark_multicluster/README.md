# This project will create Spark cluster in Docker

Use below commands-
1. cd spark-cluster
2. docker-compose up
3. cd ..
4. docker cp sample_data spark-master:/tmp/
5. docker cp sample_data_processing.py spark-master:/tmp/
6. docker exec -it spark-master
7. ./bin/spark-submit /tmp/sample_data_processing.py

if spark-submit throws error then use below command to replace pyspark file in Spark 

8. docker cp pyspark spark-master:/opt/bitnami/spark/bin/
9. ./bin/spark-submit /tmp/sample_data_processing.py
