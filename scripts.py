from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def calculate_gc_content(seq):
    gc_count = seq.count('G') + seq.count('C')
    return (gc_count / len(seq)) * 100 if len(seq) > 0 else 0

# Master reads the FASTA file and distributes sequences
if rank == 0:
    print(f"[Master] Reading FASTA file and distributing sequences to {size} processes...\n")
    sequences = []
    with open("bioinfo_data/sequences.fasta", "r") as f:
        current_seq = ""
        for line in f:
            if line.startswith(">"):
                if current_seq:
                    sequences.append(current_seq)
                    current_seq = ""
            else:
                current_seq += line.strip()
        if current_seq:
            sequences.append(current_seq)

    # Ensure data balance with the number of processes
    while len(sequences) < size:
        sequences.append("") 
    chunks = [sequences[i::size] for i in range(size)]
else:
    chunks = None

# Scatter the sequences to nodes
local_seqs = comm.scatter(chunks, root=0)

# Each node calculates GC-Content locally in parallel
for seq in local_seqs:
    if seq:
        gc_val = calculate_gc_content(seq)
        print(f"[Node: {MPI.Get_processor_name()} | Rank: {rank}] Analyzed sequence: {seq} -> GC Content: {gc_val:.2f}%")