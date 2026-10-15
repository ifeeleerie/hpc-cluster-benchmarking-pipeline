# HPC Cluster Benchmarking Automation & Telemetry Isolation Pipeline

An automated testing framework built for the **Cirrus Supercomputer (EPCC)** to orchestrate execution, audit verification logs, and isolate precise performance-per-watt telemetry for HPL and HPCG workloads.

## 🚀 Key Framework Features

* 🛠️ **Combinatorial Parameter Sweeper (`automation/`):** Algorithmic SLURM execution engine that generates parameter-tested script configurations across multiple node boundaries.
* ⚡ **Telemetry Window Isolation (`parser/`):** Custom analytical log scraper that bypasses broad whole-job Slurm energy pollution by capturing the true, localized runtime window.
* 📊 **Automated Visual Analytics Dashboard (`analysis/`):** Built-in Pandas/Matplotlib engine that converts structured log tables directly into slide-ready scaling charts.

## 📂 System Architecture
```text
├── README.md                 # System documentation & architectural roadmap
├── results.csv               # Processed experiment 3 dataset (MPI vs OpenMP)
├── autotune_results_unified.csv # Output database following schema translation
├── automation/
│   ├── sweep.py              # Combinatorial SLURM configuration generator
│   ├── provenance.py         # Git & compiler module hash metadata engine
│   └── replicate.py          # Auto-incrementing path router for repeat runs
├── parser/
│   ├── parse.py              # Window-isolated runtime & validation log scraper
│   └── converter.py          # Legacy-to-autotuner data transformation tool
└── analysis/
    └── plot.py               # Automated matplotlib performance scaling chart generator
```

## 🛠️ Cluster Deployment

Ensure your environment path is configured with the standard data analytics structures on Cirrus before triggering the visualization modules:

```bash
# Move into private secured workspace
cd ~/hpc-cluster-benchmarking-pipeline

# Load core system paths and resolve version dependency binds
module load python
pip3 install --user --upgrade "numpy<2" pandas matplotlib

# Run the system validation checks
python3 automation/provenance.py
python3 automation/replicate.py
python3 parser/converter.py
```
