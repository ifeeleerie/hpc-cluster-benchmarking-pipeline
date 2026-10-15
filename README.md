# HPC Cluster Benchmarking Automation & Telemetry Isolation Pipeline

An automated testing framework built for the **Cirrus Supercomputer (EPCC)** to orchestrate execution, audit verification logs, and isolate precise performance-per-watt telemetry for HPL and HPCG workloads.

## 🚀 Key Framework Features

* 🛠️ **Combinatorial Parameter Sweeper (`automation/`):** Algorithmic SLURM execution engine that generates parameter-tested script configurations across multiple node boundaries.
* ⚡ **Telemetry Window Isolation (`parser/`):** Custom analytical log scraper that bypasses broad whole-job Slurm energy pollution by capturing the true, localized runtime window.
* 📊 **Automated Visual Analytics Dashboard (`analysis/`):** Built-in Pandas/Matplotlib engine that converts structured log tables directly into slide-ready scaling charts.

## 📂 System Architecture
```text
├── README.md               # Pipeline documentation & operational layout
├── results.csv             # Structured telemetry database file
├── automation/
│   └── sweep.py            # Automated SLURM execution generation script
├── parser/
│   └── parse.py            # Precision regex energy extraction engine
└── analysis/
    └── plot.py             # Automatic matplotlib scaling graph generator
```

## 🛠️ Cluster Deployment

Ensure your environment path is configured with the standard data analytics structures on Cirrus before triggering the visualization modules:

```bash
# Load environmental library paths
module load python
pip3 install --user pandas matplotlib

# Run the visualization pipeline tool
python3 analysis/plot.py
```
