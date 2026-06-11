from mpi4py import MPI
from sklearn.datasets import load_digits
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import numpy as np

comm = MPI.COMM_WORLD

rank = comm.Get_rank()
size = comm.Get_size()

# Master process loads and distributes the dataset
if rank == 0:
    digits = load_digits()

    X = digits.data
    y = digits.target

    X_chunks = np.array_split(X, size)
    y_chunks = np.array_split(y, size)

    print(f"[MASTER] Dataset split into {size} chunks")

else:
    X_chunks = None
    y_chunks = None

# Scatter data across all processes
X_local = comm.scatter(X_chunks, root=0)
y_local = comm.scatter(y_chunks, root=0)

print(f"[Rank {rank}] Processing {len(X_local)} samples")

# Local model training
model = DecisionTreeClassifier()
model.fit(X_local, y_local)

# Local evaluation
predictions = model.predict(X_local)
accuracy = accuracy_score(y_local, predictions)

# Gather accuracies from all processes
all_accuracies = comm.gather(accuracy, root=0)

# Master process reports final results
if rank == 0:
    average_accuracy = np.mean(all_accuracies)

    print("\n==============================")
    print("Distributed Machine Learning Results")
    print("==============================")
    print(f"Average Accuracy: {average_accuracy * 100:.2f}%")
    print("[SUCCESS] Distributed ML Training Complete!")