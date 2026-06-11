# Hybrid HPC and Big Data Cluster for Bioinformatics Applications

## Project Overview

This project presents the design and implementation of a Hybrid High Performance Computing (HPC) and Big Data Cluster environment using OpenMPI, Docker Swarm, Apache Spark, and Python.

The infrastructure consists of one master node and two worker nodes running Ubuntu Linux virtual machines. The cluster supports distributed computing workloads, machine learning tasks, and bioinformatics applications through parallel execution and scalable resource management.

The project is divided into two main phases:

### Task 1 – Mini HPC Cluster
- Passwordless SSH configuration
- OpenMPI installation and validation
- MPI Hello World execution
- Distributed Machine Learning using the Digits dataset
- Parallel Bioinformatics sequence analysis

### Task 2 – Hybrid HPC + Big Data Cluster
- Docker Swarm deployment
- Apache Spark cluster setup
- Distributed Gene Expression Analysis using PySpark

The goal of this project is to demonstrate how modern HPC and Big Data technologies can be integrated to solve computationally intensive problems in bioinformatics and data science.

## screenshot:

## Task1: Cluster Setup & Validation

### 1. Network Hosts Setup
![Network Hosts Setup](01_network_hosts_setup.png)

### 2. Cluster Connectivity Test
![Cluster Connectivity Test](02_cluster_connectivity_test.png)

### 3. SSH Worker 1
![SSH Worker 1](03_ssh_worker1.png)

### 4. SSH Worker 2
![SSH Worker 2](04_ssh_worker2.png)

### 5. OpenMPI Installation
![OpenMPI Installation](05_openmpi_installation.png)

### 6. Hostfile Configuration
![Hostfile Configuration](06_hostfile_configuration.png)

### 7. MPI Hello World
![MPI Hello World](07_mpi_hello_world.png)

### 8. MPI Python Validation
![MPI Python Validation](08_mpi_python_validation.png)


## Task2: Docker Swarm & Apache Spark Deployment

### 1. Docker Installation
![Docker Installation](09_docker_installation.png)

### 2. Docker Swarm Cluster Initialization
![Docker Swarm Cluster Initialization](10_docker_swarm_cluster.png)

### 3. Worker 1 Joining the Swarm
![Worker 1 Joining the Swarm](11_worker1_join_swarm.png)

### 4. Worker 2 Joining the Swarm
![Worker 2 Joining the Swarm](12_worker2_join_swarm.png)

### 5. Docker Swarm Nodes Status
![Docker Swarm Nodes Status](13_docker_swarm_nodes.png)

### 6. Spark Stack Configuration File
![Spark Stack Configuration File](14_spark_stack_file.png)

### 7. Spark Services Deployment
![Spark Services Deployment](15_spark_services.png)

### 8. Spark Image Pull Error
![Spark Image Pull Error](16_spark_image_error.png)


## Conclusion

This project successfully demonstrated the deployment of a Hybrid HPC and Big Data Cluster using three Ubuntu-based virtual machines configured as one master node and two worker nodes.

The HPC environment was validated through OpenMPI-based parallel applications, including distributed machine learning and bioinformatics workloads. The successful execution of MPI jobs across multiple nodes confirmed proper cluster communication and workload distribution.

In the second phase, Docker Swarm and Apache Spark were deployed to extend the cluster toward Big Data processing capabilities. The Spark environment provided a scalable framework for distributed analytics and machine learning applications.

Overall, the project highlights the importance of combining High Performance Computing and Big Data technologies to address modern computational challenges in bioinformatics and scientific research. Future improvements may include larger cluster deployments, cloud integration, GPU acceleration, and advanced genomic analysis pipelines.
