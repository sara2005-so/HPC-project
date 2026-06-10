version: '3.8'

services:
  spark-master:
    image: bitnami/spark:3.5.0
    environment:
      - SPARK_MODE=master
    ports:
      - target: 8080
        published: 8080
        protocol: tcp
        mode: host
      - target: 7077
        published: 7077
        protocol: tcp
        mode: host
    deploy:
      placement:
        constraints:
          - node.role == manager
    networks:
      - spark-net

  spark-worker:
    image: bitnami/spark:3.5.0
    environment:
      - SPARK_MODE=worker
      - SPARK_MASTER_URL=spark://192.168.64.4:7077
    ports:
      - target: 8081
        published: 8081
        protocol: tcp
        mode: host
    deploy:
      replicas: 2
      placement:
        constraints:
          - node.role == worker
    networks:
      - spark-net

networks:
  spark-net:
    driver: overlay
    attachable: true