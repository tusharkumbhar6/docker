#!/bin/bash

# Create the logs directory if it doesn't exist
mkdir -p /opt/bitnami/spark/logs

# Start the history server
/opt/bitnami/spark/bin/spark-class org.apache.spark.deploy.history.HistoryServer \
    -Dspark.history.fs.logDirectory=/opt/bitnami/spark/logs \
    -Dspark.history.ui.port=18080
