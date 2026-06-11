version: "3.8"

services:

  spark-master:
    image: apache/spark:latest
    command: >
      /opt/spark/bin/spark-class
      org.apache.spark.deploy.master.Master
    ports:
      - "8080:8080"
      - "7077:7077"
    deploy:
      placement:
        constraints:
          - node.hostname == master

  spark-worker1:
    image: apache/spark:latest
    command: >
      /opt/spark/bin/spark-class
      org.apache.spark.deploy.worker.Worker
      spark://master:7077
    deploy:
      placement:
        constraints:
          - node.hostname == worker1

  spark-worker2:
    image: apache/spark:latest
    command: >
      /opt/spark/bin/spark-class
      org.apache.spark.deploy.worker.Worker
      spark://master:7077
    deploy:
      placement:
        constraints:
          - node.hostname == worker2