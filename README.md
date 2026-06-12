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


The cluster consists of three nodes:

- Master Node
- Worker Node 1
- Worker Node 2

---

# 1. Network Configuration

The first step was configuring the cluster network and hostname resolution across all nodes.

![Network Setup](01_network_hosts_setup.png)

Cluster connectivity was then verified between all nodes.

![Cluster Connectivity](02_cluster_connectivity_test.png)

---

# 2. SSH Configuration

Passwordless SSH access was configured from the master node to Worker 1.

![SSH Worker1](03_ssh_worker1.png)

Passwordless SSH access was also configured to Worker 2.

![SSH Worker2](04_ssh_worker2.png)

---

# 3. OpenMPI Installation and Validation

OpenMPI was installed on all nodes.

![OpenMPI Installation](05_openmpi_installation.png)

A shared hostfile was then configured.

![Hostfile Configuration](06_hostfile_configuration.png)

MPI communication was validated using a simple Hello World application.

![MPI Hello World](07_mpi_hello_world.png)

Python MPI support (mpi4py) was verified successfully.

![MPI Python Validation](08_mpi_python_validation.png)

---

# 4. Docker Swarm Cluster Deployment

Docker was installed on all cluster nodes.

![Docker Installation](09_docker_installation.png)

A Docker Swarm manager node was initialized.

![Docker Swarm Cluster](10_docker_swarm_cluster.png)

Worker1 joined the Swarm cluster.

![Worker1 Join Swarm](11_worker1_join_swarm.png)

Worker2 joined the Swarm cluster.

![Worker2 Join Swarm](12_worker2_join_swarm.png)

The cluster nodes were successfully registered.

![Docker Swarm Nodes](13_docker_swarm_nodes.png)

---

# 5. Apache Spark Deployment

A Spark stack configuration file was prepared for deployment.

![Spark Stack File](14_spark_stack_file.png)

## Deployment Issue Encountered

During deployment, an image-related issue was encountered.

![Spark Image Error](15_spark_image_error.png)

The configuration was corrected and deployment was attempted again.

![Spark Deployment Attempt](16_spark_deployment_attempt.png.png)

The Spark cluster was then successfully deployed.

![Spark Cluster Running](17_spark_cluster_running.png)

The Spark Web UI confirmed that all services were operational.

![Spark Web UI](18_spark_web_ui.png)

Spark Master Web Interface:
A screenshot of the Apache Spark Master Web UI accessed through the browser. The interface confirms the successful deployment of the Spark cluster on Docker Swarm and displays the active Spark Master service along with the cluster monitoring dashboard.

---

# 6. Distributed Gene Expression Analysis using Spark

PySpark was installed and configured.

![PySpark Installation](19_pyspark_installation.png)

The leukemia gene expression dataset was prepared.

![Gene Expression Dataset](20_gene_expression_dataset.png)

A distributed PySpark analysis script was created.

![Gene Expression Script](21_gene_expression_script_created.png)

The model was executed successfully and produced classification results.

![Gene Expression Results](22_gene_expression_results.png)

Result:

- Logistic Regression Classification
- Distributed Spark Execution
- Accuracy = 100%

---

# 7. Distributed Bioinformatics Analysis using MPI

A FASTA dataset containing DNA sequences was distributed across multiple MPI processes.

The application calculated GC Content in parallel across the cluster nodes.

![MPI GC Content Distributed](23_MPI_GC_Content_Distributed.png)

The experiment utilized six MPI processes across the cluster infrastructure, enabling concurrent analysis of DNA sequences. The successful execution on multiple nodes verified inter-node communication, workload distribution, and the effectiveness of MPI for bioinformatics applications.


Features:

- MPI Scatter Distribution
- Multi-node Execution
- Parallel DNA Sequence Analysis
- GC Content Calculation

---

# Source Files

```text
bioinfo_parallel.py
distributed_gene_expression_analysis.py
distributed_mnist.py
test_mpi.py
spark-stack.yml
hostfile
```

# Datasets

```text
bioinfo_data/
├── sequences.fasta
└── leukemia_expression.csv
```

# Technologies Used

- Ubuntu Linux
- OpenMPI
- mpi4py
- Python
- Scikit-Learn
- Docker
- Docker Swarm
- Apache Spark
- PySpark

# Learning Outcomes

This project provided practical experience in:

- HPC Cluster Deployment
- Distributed Computing
- Parallel Machine Learning
- Bioinformatics Analysis
- Docker Orchestration
- Apache Spark Deployment
- Hybrid HPC and Big Data Integration

# Conclusion

This project successfully demonstrated the deployment of a Hybrid HPC and Big Data Cluster using three Ubuntu-based virtual machines configured as one master node and two worker nodes.

The HPC environment was validated through OpenMPI-based parallel applications, including distributed machine learning and bioinformatics workloads. The successful execution of MPI jobs across multiple nodes confirmed proper cluster communication and workload distribution.

In the second phase, Docker Swarm and Apache Spark were deployed to extend the cluster toward Big Data processing capabilities. The Spark environment provided a scalable framework for distributed analytics and machine learning applications.

Overall, the project highlights the importance of combining High Performance Computing and Big Data technologies to address modern computational challenges in bioinformatics and scientific research. Future improvements may include larger cluster deployments, cloud integration, GPU acceleration, and advanced genomic analysis pipelines.
