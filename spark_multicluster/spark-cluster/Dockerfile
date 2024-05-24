FROM bitnami/spark:3.2.1

USER root

# Install Python packages
RUN apt-get update && apt-get install -y python3-pip && \
    pip3 install py4j pyspark

# Copy the start-history-server.sh script and set permissions
COPY start-history-server.sh /opt/bitnami/spark/start-history-server.sh
RUN chmod +x /opt/bitnami/spark/start-history-server.sh

USER 1001

