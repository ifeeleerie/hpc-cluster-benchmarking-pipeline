import os

# Define configurations to test (1, 2, and 4 nodes)
node_counts = [1, 2, 4]
tasks_per_node = [36]  # Test standard core distribution
omp_threads = [1]      # Threads per task

# Base SLURM template targeting Cirrus
slurm_template = """#!/bin/bash
#SBATCH --job-name={job_name}
#SBATCH --nodes={nodes}
#SBATCH --ntasks-per-node={tasks}
#SBATCH --cpus-per-task={threads}
#SBATCH --time=00:35:00
#SBATCH --exclusive
#SBATCH --partition=standard
#SBATCH --qos=standard

# Load required modules for your benchmark run
module load intel-compilers
module load mpt

export OMP_NUM_THREADS={threads}

echo "Starting job {job_name} on $SLURM_JOB_NUM_NODES nodes"

# Run your target benchmark binary here
# mpiexec ./xhpl > hpl_output_{nodes}nodes.log
"""

def generate_scripts():
    for nodes in node_counts:
        for tasks in tasks_per_node:
            for threads in omp_threads:
                job_name = f"hpl_sweep_{nodes}n_{tasks}t"
                script_content = slurm_template.format(
                    job_name=job_name,
                    nodes=nodes,
                    tasks=tasks,
                    threads=threads
                )
                filename = f"automation/run_{job_name}.slurm"
                with open(filename, "w") as f:
                    f.write(script_content)
                print(f"Generated submission script: {filename}")

if __name__ == "__main__":
    generate_scripts()
