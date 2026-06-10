# Mini-HPC and Hybrid | HPC-Big Data Clusters

## Overview
This project involves setting up a 3-node Mini-HPC Cluster on virtual machines. The infrastructure is orchestrated using Docker Swarm, and distributed data analysis is performed using Apache Spark to analyze gene expression datasets.

## Deliverables Included
- **Infrastructure:** Configured 3-node cluster with Passwordless SSH.
- **Orchestration:** Docker Swarm stack deploying Spark master and worker nodes.
- **Analysis:** Distributed Python script (`final_analysis.py`) for processing bioinformatics data.

## Project Structure
- `hostfile`: Contains the IP addresses of the cluster nodes.
- `spark-stack.yml`: The Docker stack configuration file.
- `scripts/`: Contains the analysis script.
- `screenshots/`: Visual evidence of the setup and execution steps.
- `reports/`: Detailed project analysis report.

## How to Deploy
1. Ensure the cluster is initialized: `docker swarm init`
2. Deploy the stack: `docker stack deploy -c spark-stack.yml spark`
3. Execute the analysis: `python3 scripts/final_analysis.py`

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


## Task2: Execution and Analysis Flow

### 1. Docker Swarm Initialization
![Docker Swarm Initialization](<Final Analysis Results.png>)

### 2. Spark Stack Deployment
![Spark Stack Deployment](<Spark Stack Deployment.png>)

### 3. Image Pull Errors
![Image Pull Errors](<Image Pull Errors.png>)

### 4. Successful Containers Status
![Successful Containers Status](<Successful Containers Status.png>)

### 5. Final Analysis Results
![Final Analysis Results](<Docker Swarm Initialization.png>)

