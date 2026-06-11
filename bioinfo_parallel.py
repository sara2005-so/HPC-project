from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


def calculate_gc_content(sequence):
    gc_count = sequence.count("G") + sequence.count("C")
    return (gc_count / len(sequence)) * 100 if len(sequence) > 0 else 0


# Master process reads the FASTA file and distributes sequences
if rank == 0:
    print(f"[MASTER] Reading FASTA file and distributing sequences to {size} processes...\n")

    sequences = []

    with open("bioinfo_data/sequences.fasta", "r") as fasta_file:
        current_sequence = ""

        for line in fasta_file:
            if line.startswith(">"):
                if current_sequence:
                    sequences.append(current_sequence)
                    current_sequence = ""
            else:
                current_sequence += line.strip()

        if current_sequence:
            sequences.append(current_sequence)

    # Ensure balanced distribution across processes
    while len(sequences) < size:
        sequences.append("")

    chunks = [sequences[i::size] for i in range(size)]

else:
    chunks = None


# Distribute sequences to worker processes
local_sequences = comm.scatter(chunks, root=0)

# Each process calculates GC Content in parallel
for sequence in local_sequences:
    if sequence:
        gc_content = calculate_gc_content(sequence)

        print(
            f"[Node: {MPI.Get_processor_name()} | Rank: {rank}] "
            f"Analyzed Sequence: {sequence} "
            f"-> GC Content: {gc_content:.2f}%"
        )