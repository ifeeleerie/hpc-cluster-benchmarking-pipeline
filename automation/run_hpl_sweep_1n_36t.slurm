#!/bin/bash
#SBATCH --job-name=hpl_sweep_1n_36t
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=36
#SBATCH --cpus-per-task=1
#SBATCH --time=00:35:00
#SBATCH --exclusive
#SBATCH --partition=standard
#SBATCH --qos=standard

# Load required modules for your benchmark run
module load intel-compilers
module load mpt

export OMP_NUM_THREADS=1

echo "Starting job hpl_sweep_1n_36t on $SLURM_JOB_NUM_NODES nodes"

# Run your target benchmark binary here
# mpiexec ./xhpl > hpl_output_1nodes.log
